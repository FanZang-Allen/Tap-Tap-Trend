""" This file is part of Tap Tap Web Scraper

Local web sever to handle good read user system api request
"""
from flask import request
from BackEnd.database import database, exist_in_collection
from BackEnd import user_system
from BackEnd import web_api_utility
from BackEnd.web_api import app


@app.route('/api/user/add', methods=['POST'])
def sign_up_user():
    """
    Add one user to user system
    :return: Success response or error message
    """
    if request.content_type != "application/json":
        return {"Error_message": "Content type should be application/json"}, 415
    sign_up_dict = web_api_utility.check_valid_sign_up_info()
    if sign_up_dict is None:
        return {"Error_message": "Provided body is invalid"}, 400
    uid = user_system.add_user(sign_up_dict['user_name'], sign_up_dict['password'])
    return {'Response': f'Your uid is {uid}. Please remember it.'}, 200


@app.route('/api/user/password', methods=['GET'])
def get_user_password():
    """
    Get user password with given uid
    :return: password or error message
    """
    request_uid = web_api_utility.check_valid_user_id()
    if request_uid is None:
        return {"Error_message": "Query arg id is not valid"}, 400
    query_cursor = database['User'].find({'id': request_uid}, {'password': 1, '_id': 0})
    password = list(query_cursor)[0]['password']
    return {'Query Result': password}, 200


@app.route('/api/user/password', methods=['PUT'])
def change_user_password():
    """
    Change user password with given uid
    :return: Success response or error message
    """
    uid = web_api_utility.check_valid_user_id()
    if uid is None:
        return {"Error_message": "Query arg id is not valid"}, 400
    new_password = request.args.get('password', None)
    if new_password is None:
        return {"Error_message": "Query arg password not exist"}, 400
    user_system.change_password(uid, new_password)
    return {'Response': f'user with uid {uid} changes password to {new_password}'}, 200


@app.route('/api/user/name', methods=['PUT'])
def change_user_name():
    """
    Change user name with given uid
    :return: Success response or error message
    """
    uid = web_api_utility.check_valid_user_id()
    if uid is None:
        return {"Error_message": "Query arg id is not valid"}, 400
    new_name = request.args.get('name', None)
    if new_name is None:
        return {"Error_message": "Query arg password not exist"}, 400
    user_system.change_user_name(uid, new_name)
    return {'Response': f'user with uid {uid} changes name to {new_name}'}, 200


@app.route('/api/user/info', methods=['GET'])
def get_user_info():
    """
    Get all user information with given id
    :return: query result or error message
    """
    request_uid = web_api_utility.check_valid_user_id()
    if request_uid is None:
        return {"Error_message": "Query arg id is not valid"}, 400
    query_cursor = database['User'].find({'id': request_uid}, {'_id': 0})
    return {'Query Result': list(query_cursor)}, 200


@app.route('/api/user/favourite', methods=['PUT'])
def add_user_favourite():
    """
    Add 1 game to user favourite game list
    :return: Success response or error message
    """
    info_list = web_api_utility.check_valid_favourite_arg()
    if info_list is None:
        return {"Error_message": "Query arg user_id/game_id are not valid"}, 400
    if not exist_in_collection(info_list[1], 'Game'):
        return {"Error_message": "Game with this id not exist in databse"}, 400
    user_system.add_favourite_game(info_list[0], info_list[1])
    return {'Response': f"Game {info_list[1]} added to user {info_list[0]} favourite"}, 200


@app.route('/api/user/favourite', methods=['DELETE'])
def remove_user_favourite():
    """
    Remove 1 game from user favourite game list
    :return: Success response or error message
    """
    info_list = web_api_utility.check_valid_favourite_arg()
    if info_list is None:
        return {"Error_message": "Query arg user_id/game_id are not valid"}, 400
    status = user_system.remove_favourite_game(info_list[0], info_list[1])
    if status is False:
        return {"Error_message": "User doesn't have this game in favourite list"}, 400
    return {'Response': f"Game {info_list[1]} remove from user {info_list[0]} favourite"}, 200


if __name__ == "__main__":
    app.run(debug=True)