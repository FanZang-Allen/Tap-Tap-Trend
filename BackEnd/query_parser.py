""" This file is part of Tap Tap Scraper

Query parser analyse the given query string and generate query expression
for database if valid. Return None if parse failed due to invalid input string
Query String Example:    Genre: RPG AND !JRPG AND Card; Rating: > 7.0
"""
import re
from BackEnd import common_utility


def parse_query_string(input_str: str):
    """
    Main function to parsed a input string and return None if failed
    :param input_str: string that needed to be parsed
    :return: query expression or None if input str is invalid
    """
    if input_str is None or input_str.strip() == '':
        return None
    genre_pattern = re.compile("^Genre:.*$")
    rating_pattern = re.compile("^Rating:.*$")
    split_result = input_str.split(';', 1)
    first_command = split_result[0].strip()
    if genre_pattern.match(first_command):
        remove_genre_str = first_command.split(':')[1].strip()
        first_result = parse_genre_query(remove_genre_str)
    elif rating_pattern.match(first_command):
        remove_rating_str = first_command.split(':')[1].strip()
        first_result = parse_rating_query(remove_rating_str)
    else:
        return None
    if len(split_result) != 1:
        left_result = parse_query_string(split_result[1])
        if left_result is not None:
            return {'$and': [first_result, left_result]}
    return first_result


def parse_genre_query(input_str: str):
    """
    Parse genre query part
    :param input_str: string that needed to be parsed
    :return: query expression or None if input str is invalid
    """
    if input_str is None or input_str.strip() == '':
        return None
    split_result = input_str.split('AND', 1)
    first_genre = split_result[0].strip()
    use_not = False
    # ! represent NOT in query string
    if first_genre.startswith('!'):
        use_not = True
        first_genre = first_genre[1:].strip()
    if use_not:
        first_exp = {'genre': {'$not': {"$regex": first_genre}}}
    else:
        first_exp = {'genre': {"$regex": first_genre}}
    if len(split_result) != 1:
        remained_exp = parse_genre_query(split_result[1])
        if remained_exp is not None:
            return {'$and': [first_exp, remained_exp]}
    return first_exp


def parse_rating_query(input_str: str):
    """
    Parse rating query part
    :param input_str: string that needed to be parsed
    :return: query expression or None if input str is invalid
    """
    if input_str is None or input_str.strip() == '':
        return None
    greater_pattern = re.compile("^>")
    smaller_pattern = re.compile("^<")
    input_str = input_str.strip()
    compare_op = None
    remove_comparison_str = None
    if greater_pattern.match(input_str):
        compare_op = '$gt'
        remove_comparison_str = input_str.replace('>', '', 1).strip()
    elif smaller_pattern.match(input_str):
        compare_op = '$lt'
        remove_comparison_str = input_str.replace('<', '', 1).strip()
    if common_utility.check_positive(remove_comparison_str) is False:
        return None
    comp_float = float(remove_comparison_str)
    return {'$expr': {compare_op: [{'$toDouble': '$rating'}, comp_float]}}
