""" This file is part of Good Read Web Scraper

Contain function maintaining app user system.
"""
from BackEnd.database import database, add_data


def check_user_exist(user_id: str):
    """
    Check database contain given user information.
    :param user_id: user account number
    :return: True if exist
    """
    if database['User'].count_documents({'id': user_id}, limit=1) != 0:
        return True
    return False


def add_user(user_name: str, password: str):
    """
    Create user with empty favourite list.
    :param password: login password
    :param user_name: login user name
    :return: user account number(user id)
    """
    user_dict = {'user_name': user_name, 'password': password, 'favourite_list': []}
    user_id = str(database['User'].count_documents({}) + 1)
    user_dict['id'] = user_id
    add_data(user_dict, 'User')
    return user_id


def change_password(user_id: str, new_password: str):
    """
    Change password of user with given uid
    :param new_password: new password
    :param user_id: request user id
    :return: True if successfully change password
    """
    if check_user_exist(user_id):
        database['User'].update_one({'id': user_id}, {"$set": {'password': new_password}})
        return True
    return False


def change_user_name(user_id: str, new_name: str):
    """
    Change user_name of user with given uid
    :param new_name: new name
    :param user_id: request user id
    :return: True if successfully change user_name
    """
    if check_user_exist(user_id):
        database['User'].update_one({'id': user_id}, {"$set": {'user_name': new_name}})
        return True
    return False


def add_favourite_game(user_id: str, game_id: str):
    """
    Add favourite game to favourite_list of user with given id
    :param game_id: added game's id
    :param user_id: request user id
    :return: True if successfully add game to list or game already exist
    """
    if not check_user_exist(user_id):
        return False
    query_result = database['User'].find({'id': user_id}, {'favourite_list': 1, '_id': 0})
    original_list = list(query_result)[0]['favourite_list']
    if game_id not in original_list:
        original_list.append(game_id)
    database['User'].update_one({'id': user_id}, {"$set": {'favourite_list': original_list}})
    return True


def remove_favourite_game(user_id: str, game_id: str):
    """
    Remove favourite game from favourite_list of user with given id
    :param game_id: game's id to remove
    :param user_id: request user id
    :return: True if successfully remove game from list
    """
    if not check_user_exist(user_id):
        return False
    query_result = database['User'].find({'id': user_id}, {'favourite_list': 1, '_id': 0})
    original_list = list(query_result)[0]['favourite_list']
    if game_id in original_list:
        original_list.remove(game_id)
    else:
        return False
    database['User'].update_one({'id': user_id}, {"$set": {'favourite_list': original_list}})
    return True
