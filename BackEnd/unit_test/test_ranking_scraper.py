"""
Scraper test may take several seconds
Please wait for driver to open the url and scrape the result
"""
from unittest import TestCase
from BackEnd import ranking_scraper
from BackEnd import web_driver


class TestGenreScraper(TestCase):
    """
    Class containing all test about ranking scraper
    """
    def test_scrape_region_name(self):
        """
        Test region name list is scraped correctly
        """
        web_driver.driver_open_url(ranking_scraper.RANKING_URL, False)
        web_driver.driver_click_button(ranking_scraper.DROP_DOWN_XPATH)
        parsed_html = web_driver.get_driver_html()
        result = ranking_scraper.scrape_region_list(parsed_html)
        self.assertIsNotNone(result)

    def test_get_region_id(self):
        """
        Test region id generation function works correctly
        """
        result = ranking_scraper.get_region_id('USA')
        self.assertEqual(result, 0)

    def test_scrape_one_region(self):
        """
        Test ranking list of one region is scraped correctly
        """
        result = ranking_scraper.scrape_region_ranking('USA')
        self.assertIsNotNone(result)
        self.assertEqual(result['region'], 'USA')
        self.assertIsNotNone(result['id_list'])
        self.assertIsNotNone(result['name_list'])
