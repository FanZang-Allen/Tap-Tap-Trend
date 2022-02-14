"""
Scraper test may take several seconds
Please wait for driver to open the url and scrape the result
"""
from unittest import TestCase
from BackEnd import game_scraper
from BackEnd import web_driver

TEST_GAME_URL = 'https://www.taptap.io/app/191001'
TEST_REVIEW_URL = 'https://www.taptap.io/review/2148583735'
TEST_POST_URL = 'https://www.taptap.io/moment/202309024325050002'


class TestGameScraper(TestCase):
    """
    Class containing all test about game scraper
    """
    def test_scrape_game_name(self):
        """
        Test game name is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_name(parsed_html)
        self.assertEqual('Genshin Impact', result)

    def test_scrape_game_region(self):
        """
        Test game region is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_region(parsed_html)
        self.assertEqual('Global', result.strip())

    def test_scrape_game_genre(self):
        """
        Test game genre list is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_genre(parsed_html)
        self.assertIsNotNone(result)

    def test_scrape_game_rating(self):
        """
        Test game rating is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_rating(parsed_html)
        self.assertIsNotNone(result)

    def test_scrape_game_provider(self):
        """
        Test game provider is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_provider(parsed_html)
        self.assertEqual('miHoYo', result.strip())

    def test_scrape_game_downloads(self):
        """
        Test game downloads number is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_downloads(parsed_html)
        self.assertIsNotNone(result)
        self.assertGreater(int(result), 1857354)

    def test_scrape_game_followers(self):
        """
        Test game follower number is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_followers(parsed_html)
        self.assertIsNotNone(result)
        self.assertGreater(int(result), 551121)

    def test_scrape_game_logo(self):
        """
        Test game logo url is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_logo(parsed_html)
        self.assertIsNotNone(result)

    def test_scrape_game_intro(self):
        """
        Test game intro content is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL, True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_game_intro(parsed_html)
        self.assertIsNotNone(result)

    def test_scrape_game_review_link(self):
        """
        Test game review link list is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL + '/review?sort=new', True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_reviews_link(parsed_html)
        self.assertIsNotNone(result)
        review_link_base = 'https://www.taptap.io/review/'
        for link in result:
            self.assertTrue(link.startswith(review_link_base))

    def test_scrape_game_review(self):
        """
        Test game review dict is scraped correctly
        """
        result = game_scraper.scrape_game_reviews([TEST_REVIEW_URL])
        self.assertIsNotNone(result)
        for info in result:
            self.assertIsNotNone(info['reviewer'])
            self.assertIsNotNone(info['avatar_url'])
            self.assertIsNotNone(info['review_time'])
            self.assertIsNotNone(info['rating'])
            self.assertIsNotNone(info['content'])

    def test_scrape_game_post_link(self):
        """
        Test game post link list is scraped correctly
        """
        web_driver.driver_open_url(TEST_GAME_URL + '/topic?sort=created', True)
        parsed_html = web_driver.get_driver_html()
        result = game_scraper.scrape_posts_link(parsed_html)
        self.assertIsNotNone(result)
        post_link_base = 'https://www.taptap.io/moment/'
        for link in result:
            self.assertTrue(link.startswith(post_link_base))

    def test_scrape_game_post(self):
        """
        Test game review dict is scraped correctly
        """
        result = game_scraper.scrape_game_posts([TEST_POST_URL])
        self.assertIsNotNone(result)
        for info in result:
            self.assertIsNotNone(info['poster'])
            self.assertIsNotNone(info['avatar_url'])
            self.assertIsNotNone(info['post_time'])
            self.assertIsNotNone(info['type'])
            self.assertIsNotNone(info['content'])
