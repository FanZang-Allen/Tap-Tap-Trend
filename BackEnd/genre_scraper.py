""" This file is part of Tap Tap Scraper

Contain functions that scrape common genres in Tap Tap
and scrape popular games in each genre
"""
from BackEnd.database import database, add_data
from BackEnd import web_driver
from BackEnd.game_scraper import scrape_game

GENRE_BASE_URL = 'https://www.taptap.io/tag/'
GAME_BASE_URL = 'https://www.taptap.io/app/'
COMMON_GENRE_URL = 'https://www.taptap.io/categories/all'


def scrape_genre():
    """
    Main function that scrape name of genres and then scrape
    id and names of popular games in each genre
    :return: None
    """
    common_genres = scrape_common_genres()
    for genre in common_genres:
        genre_dict = scrape_one_genre(genre)
        if genre_dict is not None:
            add_data(genre_dict, 'Genre')


def scrape_common_genres():
    """
    Scrape genres names in Tap Tap Discover Tab.
    :return:None if failed, genre name list if succeed
    """
    web_driver.driver_open_url(COMMON_GENRE_URL, False)
    parsed_html = web_driver.get_driver_html()
    try:
        common_genre = []
        tag_box = parsed_html.find('div', class_='tap-column')
        class_name = 'other-cate__item-name heading-m14-w16 tap-text tap-text__one-line'
        span_list = tag_box.find_all('span', class_=class_name)
        for span in span_list:
            common_genre.append(span.text.strip())
        return common_genre
    except (AttributeError, TypeError):
        print('common genre scrape failed')
        return None


def get_genre_id(genre: str):
    """
    Check database stored id for a specific genre
    Generate new id if no matching genre is found.
    :param genre: request name of genre
    :return: Id of document in database
    """
    query_result = database['Genre'].find({}, {'_id': 0})
    new_id = 0
    for result in query_result:
        if result['genre'] == genre:
            return result['id']
        new_id += 1
    return new_id


def get_existing_genre():
    """
    Get all genres of existing game in database
    :return: Genre name list
    """
    query_result = database['Game'].find({}, {'genre': 1, '_id': 0})
    genre_list = []
    for result in query_result:
        curr_genre = result['genre']
        genre_list = list(set(genre_list) | set(curr_genre))
    return genre_list


def scrape_one_genre(genre):
    """
    Scrape id and name of popular games in one genre
    :param genre: name of genre
    :return: Genre info dict
    """
    web_driver.driver_open_url(GENRE_BASE_URL + genre, False)
    parsed_html = web_driver.get_driver_html()
    genre_dict = {'genre': genre}
    try:
        id_list = []
        name_list = []
        ranking_box = parsed_html.find('div', class_='tap-list game-list__tap-list')
        div_list = ranking_box.find_all('div', class_='game-list-card flex-center--y')
        for div in div_list:
            title_a = div.find('a', class_='tap-router tap-app-title__wrap')
            game_id = title_a['href'].split('/')[-1]
            game_name = title_a["title"]
            id_list.append(game_id)
            name_list.append(game_name)
        genre_dict['id'] = get_genre_id(genre)
        genre_dict['id_list'] = id_list
        genre_dict['name_list'] = name_list
        return genre_dict
    except (AttributeError, TypeError):
        print('genre ranking scrape failed')
        return None


def scrape_genre_game():
    """
    Scrape detail information of games in all genres.
    Call after database contains scraped genres documents
    :return: None
    """
    print("Scraper start scraping related games in genre list.")
    query_result = database['Genre'].find({}, {'id_list': 1, '_id': 0})
    for result in query_result:
        curr_list = result['id_list']
        for game_id in curr_list:
            scrape_game(GAME_BASE_URL + game_id, False)
