"""
Scraper test may take several seconds
Please wait for driver to open the url and scrape the result
"""
from unittest import TestCase
from BackEnd import genre_scraper


class TestGenreScraper(TestCase):
    """
    Class containing all test about genre scraper
    """
    def test_scrape_common_genre(self):
        """
        Test common genre name list is scraped correctly
        """
        result = genre_scraper.scrape_common_genres()
        self.assertIsNotNone(result)

    def test_get_genre_id(self):
        """
        Test genre id generation function works correctly
        """
        result = genre_scraper.get_genre_id('Card')
        self.assertEqual(result, 0)

    def test_scrape_one_genre(self):
        """
        Test info about one genre is scraped correctly
        """
        result = genre_scraper.scrape_one_genre('Card')
        self.assertIsNotNone(result)
        self.assertEqual(result['genre'], 'Card')
        self.assertIsNotNone(result['id_list'])
        self.assertIsNotNone(result['name_list'])
