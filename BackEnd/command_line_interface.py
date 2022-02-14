""" This file is part of Tap Tap Scraper

Contain all interface functions to interactively communicate with user
Start scraper/json/api mode according to user input
"""
import requests
from BackEnd import database
from BackEnd import game_scraper
from BackEnd import genre_scraper
from BackEnd import ranking_scraper
from BackEnd import cli_utility
from BackEnd import common_utility


def start_interface():
    """
    Function that get mode of program
    :return: None
    """
    mode_hint = "scrape -- Activate scraper and stored info in database.\n" + \
                "json -- Export game & ranking & genre data to json\n" + \
                "api -- Use api to manipulate database\n\n"
    mode_valid_input = ['scrape', 'json', 'api']
    mode = input(mode_hint)
    while True:
        if cli_utility.check_valid_input(mode, mode_valid_input):
            break
        mode = input()
    if mode == 'scrape':
        scrape_mode()
    elif mode == 'json':
        json_mode()
    else:
        api_mode()


def scrape_mode():
    """
    Function that guide user to input arguments that scraper required
    :return: None
    """
    scrape_hint = "Please pick a option to start\n" + \
                  "Game -- Scrape detail info of one game using id.\n" + \
                  "Ranking -- Scrape ranking list of all regions.\n" + \
                  "Genre -- Scrape all common genres in Tap Tap.\n"
    mode_valid_input = ['Game', 'Ranking', 'Genre']
    mode = input(scrape_hint)
    while True:
        if cli_utility.check_valid_input(mode, mode_valid_input):
            break
        mode = input()
    if mode == 'Game':
        game_id_str = input('Please input a game id.\n')
        while True:
            if not common_utility.check_positive(game_id_str):
                game_id_str = input('Please provide a non negative integer.\n')
            else:
                break
        base_url = ranking_scraper.GAME_BASE_URL
        game_scraper.scrape_game(base_url + game_id_str, True)
    elif mode == 'Ranking':
        print('Ranking list scraper starts.')
        ranking_scraper.scrape_ranking()
        ranking_scraper.scrape_ranking_games()
        print('Ranking list scraper finishes.')
    else:
        print('Genre scraper starts.')
        genre_scraper.scrape_genre()
        genre_scraper.scrape_genre_game()
        print('Genre scraper finishes.')


def json_mode():
    """
    Function that guide user to input json file path and manipulate the database accordingly
    :return:None
    """
    json_option_str = "Please pick a option to start\n" + \
                      "Game -- Export detail info of one game using id.\n" + \
                      "Ranking -- Export ranking list info to a json file.\n" + \
                      "Genre -- Export games of each genre to a json file.\n"
    json_valid_input = ['Game', 'Ranking', 'Genre']
    json_option = input(json_option_str)
    while True:
        if cli_utility.check_valid_input(json_option, json_valid_input):
            break
        json_option = input()

    if json_option == 'Game':
        game_id_str = input('Please input a game id.\n')
        while True:
            if not common_utility.check_positive(game_id_str):
                game_id_str = input('Please provide a non negative integer.\n')
            elif not database.exist_in_collection(game_id_str, 'Game'):
                print('This id does not exist in database')
                game_id_str = input('Please input a game id.\n')
            else:
                break
        database.export_data_json('json_file/result.json', 'Game', [game_id_str])
    elif json_option == 'Ranking':
        database.export_data_json('json_file/result.json', 'Ranking', None)
    else:
        database.export_data_json('json_file/result.json', 'Genre', None)


def api_mode():
    """
    Function that guide user pick a api option to continue
    :return:None
    """
    api_option_str = "Please pick a mode to start\n" + \
                     "Ranking -- Get ranking list in one region along with corresponding game info\n" + \
                     "Genre -- Get list of game info in one genre\n" + \
                     "Game -- Get detail info of games by id\n" + \
                     "Search -- Get games info by query string\n" + \
                     "User -- Manipulate user system using different request\n"
    api_valid_input = ['Ranking', 'Genre', 'Game', 'Search', 'User']
    api_option = input(api_option_str)
    while True:
        if cli_utility.check_valid_input(api_option, api_valid_input):
            break
        api_option = input()
    if api_option == 'Ranking':
        request_rank()
    elif api_option == 'Genre':
        request_genre()
    elif api_option == 'Game':
        request_game()
    elif api_option == 'Search':
        request_search()
    else:
        user_mode()


def request_rank():
    """
    Function that guide user input rank request required arguments
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/rank'
    query_str = input("Please input a region name\n")
    response = requests.get(request_url, params={'region': query_str})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_genre():
    """
    Function that guide user input genre request required arguments
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/genre'
    query_str = input("Please input a genre name\n")
    response = requests.get(request_url, params={'genre': query_str})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_game():
    """
    Function that guide user input genre request required arguments
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/game'
    input_str = input("Please input games id in this format: 1,2,3\n")
    while True:
        id_list = cli_utility.check_valid_game_id_list(input_str)
        if id_list is not None:
            break
        input_str = input("Please input games id in this format: 1,2,3\n")
    response = requests.get(request_url,
                            json=id_list,
                            headers={'Content-Type': "application/json",
                                     'Accept': "application/json"})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_search():
    """
    Function that guide user input genre request required arguments
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/search'
    query_str = input("Please input a query string\n")
    response = requests.get(request_url, params={'query': query_str.strip()})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def user_mode():
    """
    Function that guide user to pick how to manipulate user system
    :return:None
    """
    api_option_str = "Please pick a number to start\n" + \
                     "1 -- Sign up a user to the system\n" + \
                     "2 -- View password of one user\n" + \
                     "3 -- Change password of one user\n" + \
                     "4 -- Add a game to favourite list of one user\n" + \
                     "5 -- Remove a game from favourite list of one user\n" +\
                     "6 -- Get all info about a user\n"
    api_valid_input = ['1', '2', '3', '4', '5', '6']
    api_option = input(api_option_str)
    while True:
        if cli_utility.check_valid_input(api_option, api_valid_input):
            break
        api_option = input()
    if api_option == '1':
        request_add_user()
    elif api_option == '2':
        request_view_password()
    elif api_option == '3':
        request_change_password()
    elif api_option == '4':
        request_add_favourite()
    elif api_option == '5':
        request_remove_password()
    else:
        request_user_info()


def request_add_user():
    """
    Function that guide user input information to sign up a user
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/user/add'
    input_name = input("Please input a user name.\n")
    input_password = input("Please input password.\n")
    json_data = {'user_name': input_name, 'password': input_password}
    response = requests.post(request_url,
                             json=json_data,
                             headers={'Content-Type': "application/json",
                                      'Accept': "application/json"})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_view_password():
    """
    Function that guide user input information to view password using uid
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/user/password'
    input_uid = input("Please input user uid.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_uid = input("Please input a valid uid.\n")
    response = requests.get(request_url, params={'id': input_uid})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_change_password():
    """
    Function that guide user to change a password given uid
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/user/password'
    input_uid = input("Please input user uid.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_uid = input("Please input a valid uid.\n")
    input_password = input("Please input new password.\n")
    response = requests.put(request_url, params={'id': input_uid, 'password':input_password})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_add_favourite():
    """
    Function that guide user to add a game to user favourite list
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/user/favourite'
    input_uid = input("Please input user uid.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_uid = input("Please input a valid uid.\n")
    input_gid = input("Please input a game id "
                      "that will be add to favourite list.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_gid = input("Please input a valid game id.\n")
    response = requests.put(request_url, params={'user_id': input_uid, 'game_id': input_gid})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_remove_password():
    """
    Function that guide user to remove a game from user favourite list
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/user/favourite'
    input_uid = input("Please input user uid.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_uid = input("Please input a valid uid.\n")
    input_gid = input("Please input a game id "
                      "that will be add to favourite list.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_gid = input("Please input a valid game id.\n")
    response = requests.delete(request_url, params={'user_id': input_uid, 'game_id': input_gid})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


def request_user_info():
    """
    Function that guide user input uid to view user info
    :return: response from server
    """
    request_url = 'http://127.0.0.1:5000/api/user/info'
    input_uid = input("Please input user uid.\n")
    while True:
        if common_utility.check_positive(input_uid):
            break
        input_uid = input("Please input a valid uid.\n")
    response = requests.get(request_url, params={'id': input_uid})
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.json())


if __name__ == '__main__':
    start_interface()
