""" This file is part of Tap Tap Scraper

Contain functions that scrape all required detail information
of one game and store collected info into database
"""
import time
from BackEnd import database
from BackEnd import web_driver

BASE_URL = 'https://www.taptap.io'


def scrape_game(url: str, update_allowed):
    """
    Main function that call other scrape functions to
    fill out the game information dict and add it to database
    :param update_allowed: control if game info allowed to be updated
    :param url: game url in Tap Tap
    :return:
    """
    info_dict = {}
    game_id = url.split('/')[-1]
    if database.exist_in_collection(game_id, 'Game') and not update_allowed:
        # if game already scarped and update not allowed
        print(f'Game {game_id} already exist')
        return None
    info_dict['id'] = game_id
    web_driver.driver_open_url(url, True)
    parsed_html = web_driver.get_driver_html()

    info_dict['name'] = scrape_game_name(parsed_html)
    info_dict['region'] = scrape_game_region(parsed_html)
    info_dict['genre'] = scrape_game_genre(parsed_html)
    info_dict['rating'] = scrape_game_rating(parsed_html)
    info_dict['provider'] = scrape_game_provider(parsed_html)
    info_dict['downloads'] = scrape_game_downloads(parsed_html)
    info_dict['followers'] = scrape_game_followers(parsed_html)
    info_dict['logo'] = scrape_game_logo(parsed_html)
    info_dict['intro'] = scrape_game_intro(parsed_html)

    web_driver.driver_open_url(url + '/review?sort=new', False)
    # To ensure the review page is fully rendered
    time.sleep(1)
    parsed_html = web_driver.get_driver_html()
    info_dict['reviews_link'] = scrape_reviews_link(parsed_html)
    info_dict['reviews'] = scrape_game_reviews(info_dict['reviews_link'])

    web_driver.driver_open_url(url + '/topic?sort=created', False)
    parsed_html = web_driver.get_driver_html()
    info_dict['posts_link'] = scrape_posts_link(parsed_html)
    info_dict['posts'] = scrape_game_posts(info_dict['posts_link'])

    database.add_data(info_dict, 'Game')
    return info_dict


def scrape_game_name(parsed_html):
    """
    Get game name from parsed html
    :param parsed_html: parsed data from web driver
    :return: game name
    """
    try:
        header_box = parsed_html.find('div', class_='header-banner__title')
        header = header_box.h1.text.strip()
        return header
    except (AttributeError, TypeError):
        print('name scrape failed')
        return None


def scrape_game_region(parsed_html):
    """
    Get game region from parsed html
    :param parsed_html: parsed data from web driver
    :return: game region str
    """
    try:
        header_div = parsed_html.find('div', class_='header-banner__title')
        span_class = 'tap-tag caption-m10-w12 font-bold ' \
                     'tap-tag--outline tap-tag--gray caption-m10-w12 ' \
                     'font-bold gray-06 tap-app-title__tag'
        region_span = header_div.find('span', class_=span_class)
        if region_span is not None:
            return region_span.text.strip()
        return None
    except (AttributeError, TypeError):
        print('region scrape failed')
        return None


def scrape_game_genre(parsed_html):
    """
    Get game genre from parsed html
    :param parsed_html: parsed data from web driver
    :return: genre list
    """
    try:
        genre = []
        tap_swiper = parsed_html.find('div', class_='web-aside-wrapper--tags')
        class_name = 'app-aside-chip__text tap-text tap-text__one-line'
        genre_div_list = tap_swiper.find_all('div', class_=class_name)
        for div in genre_div_list:
            genre.append(div.text.strip())
        return genre
    except (AttributeError, TypeError):
        print('genre scrape failed')
        return None


def scrape_game_rating(parsed_html):
    """
    Get game rating from parsed html
    :param parsed_html: parsed data from web driver
    :return: rating number
    """
    try:
        div_name = "game-info__stat--review-number app-rating__number font-bold rate-number-font"
        rating_div = parsed_html.find('div', class_=div_name)
        rating = rating_div.text.strip()
        return rating
    except (AttributeError, TypeError):
        print('rating scrape failed')
        return None


def scrape_game_provider(parsed_html):
    """
    Get game provider from parsed html
    :param parsed_html: parsed data from web driver
    :return: provider name
    """
    try:
        info_box = parsed_html.find('div', class_='game-info__text')
        provider_div = info_box.find('div', class_='tap-text-group tap-text-group--inline')
        provider = provider_div.find_all('span')[-1].text.strip()
        return provider
    except (AttributeError, TypeError):
        print('provider scrape failed')
        return None


def scrape_game_downloads(parsed_html):
    """
    Get number of downloads from parsed html
    :param parsed_html: parsed data from web driver
    :return: number of downloads
    """
    try:
        info_box = parsed_html.find('div', class_='game-info__text')
        downloads_div = info_box.find('div', class_='game-info__text-item')
        downloads_span = downloads_div.find_all('span', class_='game-info__stat--text')[0]
        downloads = downloads_span.find_all('span')[-1].text.strip()
        return downloads
    except (AttributeError, TypeError):
        print('downloads scrape failed')
        return None


def scrape_game_followers(parsed_html):
    """
    Get number of followers from parsed html
    :param parsed_html: parsed data from web driver
    :return:number of followers
    """
    try:
        info_box = parsed_html.find('div', class_='game-info__text')
        followers_div = info_box.find('div', class_='game-info__text-item')
        followers_span = followers_div.find_all('span', class_='game-info__stat--text')[1]
        followers = followers_span.find_all('span')[-1].text.strip()
        return followers
    except (AttributeError, TypeError):
        print('followers scrape failed')
        return None


def scrape_game_logo(parsed_html):
    """
    Get game logo url from parsed html
    :param parsed_html: parsed data from web driver
    :return: logo url
    """
    try:
        header_box = parsed_html.find('header', class_='app-detail__header-banner')
        logo_img = header_box.find('img', class_='origin-image')
        logo_url = logo_img['src']
        return logo_url
    except (AttributeError, TypeError):
        print('logo scrape failed')
        return None


def scrape_game_intro(parsed_html):
    """
    Get game introduction from parsed html
    :param parsed_html: parsed data from web driver
    :return: game intro text
    """
    try:
        about_box = parsed_html.find('div', class_='text-box__content text-box__content_collapsed')
        intro = about_box.find('p', class_='paragraph-m14-w14 gray-08').text.strip()
        return intro
    except (AttributeError, TypeError):
        print('intro scrape failed')
        return None


def scrape_reviews_link(parsed_html):
    """
    Get game review url list to prepare for review dict scraper
    :param parsed_html: parsed data from web driver
    :return: review url list
    """
    try:
        review_box = parsed_html.find('div', class_='tap-list app-reviews__list')
        class_name = 'tap-router review-item taptap-card taptap-card--round'
        div_list = review_box.find_all('div', class_=class_name)
        review_link_list = []
        for div in div_list:
            text_box = div.find('div', class_='text-box__content')
            link = BASE_URL + text_box.a['href']
            review_link_list.append(link)
        return review_link_list
    except (AttributeError, TypeError):
        print('review link scrape failed')
        return None


def get_review_rating(rate_div):
    """
    Get reviewer's rating of game base on svg element width.
    Helper function used in scrape_game_reviews()
    :param rate_div: rating div that contain svg width
    :return: reviewer rating about game
    """
    try:
        highlight_style = rate_div['style']
        rating_text = highlight_style.split(':')[1].strip()[:-3]
        rating = int(rating_text) / 15
        return str(rating)
    except (AttributeError, TypeError):
        return None


def scrape_game_reviews(reviews_link_list):
    """
    Get all info about a review including reviewer name,
    avatar url,review time,rating,review content, device
    and play time if available
    :param reviews_link_list: result from scrape_reviews_link()
    :return: list of all review info
    """
    review_list = []
    try:
        for link in reviews_link_list:
            review = {}
            translate_xpath = "//div[@class='tap-translate__warp']//*[name()='svg' " \
                              "and @class='svg-icon icon-ico-m20-w22-translate']"
            web_driver.driver_open_url(link, False)
            web_driver.driver_click_button(translate_xpath)
            parsed_html = web_driver.get_driver_html()
            detail_div = parsed_html.find('div', class_='review-detail-info')
            avatar = detail_div.find('div', class_='lazy-image user-avatar__image').img
            review['reviewer'] = avatar['alt']
            review['avatar_url'] = avatar['src']
            time_box = detail_div.find('div', class_='review-detail-info__user-bottom')
            review['review_time'] = time_box.span.text.strip()
            rating_class = detail_div.find('div', class_='tap-rate')
            rating_div = rating_class.find('div', class_='tap-rate__highlight')
            review['rating'] = get_review_rating(rating_div)
            content_div = detail_div.find('div', class_='review-detail__content-wrap')
            review['content'] = content_div.p.text.strip()
            device_div = parsed_html.find('div', class_='review-detail__device')
            if device_div is not None:
                device = device_div.find('div', class_='w-icon-tag__title')
                if device is not None:
                    review['device'] = device.text
                play_time = device_div.find('span', class_='review-detail__played-tips')
                if play_time is not None:
                    review['play_time'] = play_time
            review_list.append(review)
        return review_list
    except (AttributeError, TypeError):
        print('review scrape failed')
        return review_list


def scrape_posts_link(parsed_html):
    """
    Get game post url list to prepare for post dict scraper
    :param parsed_html: parsed data from web driver
    :return: list of post url for scrape_game_posts()
    """
    try:
        posts_box = parsed_html.find('div', class_='group-feed-list')
        div_list = posts_box.find_all('div', class_='tap-router moment-list-item moment-card')
        posts_link_list = []
        for div in div_list:
            text_box = div.find('a', class_='tap-router moment-image-list__wrap')
            if text_box is None:
                continue
            link = BASE_URL + text_box['href']
            posts_link_list.append(link)
        return posts_link_list
    except (AttributeError, TypeError):
        print('posts link scrape failed')
        return None


def scrape_game_posts(posts_link_list):
    """
    Get all info about a post including poster name,
    avatar url,post time,num of view of this post
    post type,and post content
    :param posts_link_list: result from scrape_posts_link()
    :return: list of post info
    """
    try:
        post_list = []
        for link in posts_link_list:
            post = {}
            translate_xpath = "//div[@class='tap-translate__warp']//*[name()='svg' " \
                              "and @class='svg-icon icon-ico-m20-w22-translate']"
            web_driver.driver_open_url(link, False)
            web_driver.driver_click_button(translate_xpath)
            parsed_html = web_driver.get_driver_html()
            header_div = parsed_html.find('div', class_='tap-router moment-detail__header-left')
            avatar = header_div.find('div', class_='moment-avatar').img
            post['avatar_url'] = avatar['src']
            post['poster'] = avatar['alt']
            time_box = header_div.find('div', class_='moment-detail__header-left-box-time')
            span_list = time_box.find_all('span')
            post['post_time'] = span_list[0].text.strip()
            post['type'] = span_list[-1].text.strip()
            if len(span_list) > 2:
                post['views'] = span_list[1].text.strip()
            content_box = parsed_html.find('div', class_='moment-detail__text')
            post['content'] = content_box.text.strip()
            post_list.append(post)
        return post_list
    except (AttributeError, TypeError):
        print('post scrape failed')
        return None
