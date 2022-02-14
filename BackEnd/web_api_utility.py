""" This file is part of Tap Tap Scraper

Contain useful function used in web_api.py
"""
from flask import request
from BackEnd.database import database, exist_in_collection
from BackEnd.user_system import check_user_exist
from BackEnd.common_utility import check_positive
from BackEnd.query_parser import parse_query_string


def check_valid_region():
    """
    Function that check if region name in request arg is valid
    :return: valid input or None
    """
    if 'region' not in request.args:
        return None
    valid_region_cursor = database['Ranking'].find({}, {'region': 1, '_id': 0})
    valid_region_list = []
    for info_dict in valid_region_cursor:
        valid_region_list.append(info_dict['region'])
    request_region = request.args.get('region', None)
    if request_region not in valid_region_list:
        return None
    return request_region


def check_valid_genre():
    """
    Function that check if genre in request arg is valid
    :return: valid input or None
    """
    if 'genre' not in request.args:
        return None
    valid_genre_cursor = database['Genre'].find({}, {'genre': 1, '_id': 0})
    valid_genre_list = []
    for info_dict in valid_genre_cursor:
        valid_genre_list.append(info_dict['genre'])
    request_genre = request.args.get('genre', None)
    if request_genre not in valid_genre_list:
        return None
    return request_genre


def check_valid_games_id():
    """
    Function that check if request body contain valid id list of games
    :return: valid input or None
    """
    data = request.get_json()
    if type(data) is not list:
        return None
    for game_id in data:
        if check_positive(game_id) is False:
            return None
    return data


def check_valid_query_str():
    """
    Function that check if genre in request arg is valid
    :return: valid input or None
    """
    if 'query' not in request.args:
        return None
    input_query = request.args.get('query', None)
    parsed_result = parse_query_string(input_query)
    return parsed_result


def check_valid_sign_up_info():
    """
    Function that check if request body contain valid user name
    and password to sign up a user
    :return: valid input or None
    """
    data = request.get_json()
    if type(data) is not dict:
        return None
    else:
        if 'user_name' not in data:
            return None
        elif 'password' not in data:
            return None
    return data


def check_valid_user_id():
    """
    Function that check if given user id in query arg is valid
    :return: valid input or None
    """
    if 'id' not in request.args:
        return None
    request_id = request.args.get('id', None)
    if not check_positive(request_id):
        return None
    if not check_user_exist(request_id):
        return None
    return request_id


def check_valid_favourite_arg():
    """
    Function that check if user provide a valid user id
    and a valid game id. Used for favourite game routes.
    :return: valid input or None
    """
    if 'user_id' not in request.args:
        return None
    if 'game_id' not in request.args:
        return None
    user_id = request.args.get('user_id', None)
    game_id = request.args.get('game_id', None)
    if not check_positive(user_id) or not check_positive(game_id):
        return None
    if not check_user_exist(user_id):
        return None
    if not exist_in_collection(game_id, "Game"):
        return None
    return [user_id, game_id]
