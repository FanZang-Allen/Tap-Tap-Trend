""" This file is part of Good Read Web Scraper

Set up selenium web driver and use BeautifulSoup to parse
rendered html in driver. Contain useful driver functions used in
all scrapers.
"""
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


def driver_open_url(url, scroll_required):
    """
    Let driver open a given url
    :param url: request url
    :param scroll_required: weather to scroll the browser to the end
    :return: None
    """
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(1)
    if scroll_required:
        # scroll browser to render image or get more content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def driver_click_button(button_xpath):
    """
    Let driver use mouse to click a button using element xpath
    :param button_xpath: xpath to element
    :return: None
    """
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, button_xpath))).click()
    time.sleep(1)


def get_driver_html():
    """
    Called after driver has opened a url, parsed rendered html of current url.
    :return: parsed html
    """
    time.sleep(1)
    html = driver.page_source
    parsed_html = BeautifulSoup(html, 'html.parser')
    return parsed_html
