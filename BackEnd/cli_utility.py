""" This file is part of Tap Tap Scraper

Contain useful function used in command_line_interface.py
"""
import os
from BackEnd.common_utility import check_positive


def check_valid_input(input_str: str, valid_list: list):
    """
    Check if input string is inside valid list
    Give hint if invalid input got
    :param input_str: string from user
    :param valid_list: contain all valid string
    :return: True if valid input is provided
    """
    if input_str not in valid_list:
        hint = "Please provide following input: "
        for text in valid_list:
            hint += text + ', '
        hint = hint[:-2]
        print(hint)
        return False
    return True


def check_valid_export_path(file_path: str):
    """
    Check if file path exist and is a json file
    :param file_path: path to be checked
    :return: True if path is valid
    """
    if os.path.exists(file_path) and file_path.endswith('.json'):
        return True
    return False


def check_valid_game_id_list(input_str: str):
    """
    Check if user input id list in correct format
    :param input_str: user input id string
    :return: id list if valid
    """
    if input_str is None or input_str.strip() == '':
        return None
    split_result = input_str.split(',')
    id_list = []
    for result in split_result:
        if not check_positive(result.strip()):
            return None
        id_list.append(result.strip())
    return id_list
