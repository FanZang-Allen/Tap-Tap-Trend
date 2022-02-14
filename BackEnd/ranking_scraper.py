""" This file is part of Tap Tap Scraper

Contain functions that scrape ranking list of each region
in Tap Tap, and scrape popular games in each genre
"""
from BackEnd.database import database, add_data
from BackEnd import web_driver
from BackEnd.game_scraper import scrape_game

GAME_BASE_URL = 'https://www.taptap.io/app/'
RANKING_URL = 'https://www.taptap.io/top/download'
DROP_DOWN_XPATH = "//div[@class='switch-region__box flex-center" \
                  " switch-region__box--hover']//*[name()='svg'" \
                  " and @class='svg-icon icon-ico-m12-w14-filledarrow-down gray-08']"


def get_region_id(region: str):
    """
    Check database stored id for a specific region
    Generate new id if no matching region is found.
    :param region: name of region
    :return: Id of document in database
    """
    query_result = database['Ranking'].find({}, {'_id': 0})
    new_id = 0
    for result in query_result:
        if result['region'] == region:
            return result['id']
        new_id += 1
    return new_id


def scrape_ranking():
    """
    Main function that scrape name of regions and then scrape
    id and names of popular games in ranking list of each region
    :return: None
    """
    web_driver.driver_open_url(RANKING_URL, False)
    web_driver.driver_click_button(DROP_DOWN_XPATH)
    parsed_html = web_driver.get_driver_html()
    region_list = scrape_region_list(parsed_html)
    if region_list is None:
        print("ranking scrape failed")
        return
    for region in region_list:
        region_dict = scrape_region_ranking(region)
        region_dict['id'] = get_region_id(region)
        add_data(region_dict, 'Ranking')


def scrape_region_list(parsed_html):
    """
    Scrape all regions name available in TapTap
    :param parsed_html: parsed data from web driver
    :return: list of region name
    """
    try:
        region_list = []
        option_box = parsed_html.find('div', class_='region-option')
        region_class = 'region-option__item__text gray-08 paragraph-m16-w16'
        region_span_list = option_box.find_all('span', class_=region_class)
        for span in region_span_list:
            region_list.append(span.text)
        return region_list
    except (AttributeError, TypeError):
        print('region list scrape failed')
        return None


def generate_region_xpath(region):
    """
    Generate region button xpath using region name
    :param region: name of region
    :return: button xpath for web driver to switch ranking list
    """
    return f"//div[@class='region-option']//*[name()='span' and text()='{region}']"


def scrape_region_ranking(region):
    """
    Scrape id and name of popular games in ranking list of a region
    :param region:name of region
    :return: region dict stroed in  database
    """
    web_driver.driver_open_url(RANKING_URL, False)
    web_driver.driver_click_button(DROP_DOWN_XPATH)
    region_xpath = generate_region_xpath(region)
    web_driver.driver_click_button(region_xpath)
    parsed_html = web_driver.get_driver_html()
    region_dict = {'region': region}
    try:
        id_list = []
        name_list = []
        ranking_box = parsed_html.find('div', class_='tap-list list-content__list')
        div_list = ranking_box.find_all('div', class_='game-card flex-center--y')
        for div in div_list:
            title_a = div.find('a', class_='tap-router tap-app-title__wrap')
            game_id = title_a['href'].split('/')[-1]
            game_name = title_a["title"]
            id_list.append(game_id)
            name_list.append(game_name)
        if len(id_list) == 0 or len(name_list) == 0:
            print('region game list is empty')
            return None
        region_dict['id_list'] = id_list
        region_dict['name_list'] = name_list
        return region_dict
    except (AttributeError, TypeError):
        print('region ranking scrape failed')
        return None


def scrape_ranking_games():
    """
    Scrape detail information of games in all regions.
    Call after database contains scraped region documents
    :return: None
    """
    print("Scraper start scraping related games in ranking list.")
    query_result = database['Ranking'].find({}, {'id_list': 1, '_id': 0})
    for result in query_result:
        curr_list = result['id_list']
        for game_id in curr_list:
            scrape_game(GAME_BASE_URL + game_id, False)
