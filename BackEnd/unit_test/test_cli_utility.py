"""
Unit test for cli_utility.py
"""
from unittest import TestCase
from BackEnd import cli_utility


class TestCLIUtility(TestCase):
    """
    Class containing all test about cli_utility
    """
    def test_check_valid_input(self):
        """
        Test check_valid_input correctly identify invalid input
        """
        valid_list = ['Game', 'Ranking']
        self.assertTrue(cli_utility.check_valid_input('Game', valid_list))
        self.assertTrue(cli_utility.check_valid_input('Ranking', valid_list))
        self.assertFalse(cli_utility.check_valid_input('Genre', valid_list))

    def test_check_valid_export_path(self):
        """
        Test check_valid_export_path correctly identify invalid json file
        """
        self.assertTrue(cli_utility.check_valid_export_path('../json_file/result.json'))
        self.assertFalse(cli_utility.check_valid_export_path('not_exist.json'))
        self.assertFalse(cli_utility.check_valid_export_path('json_file/result'))

    def test_check_valid_game_id_list(self):
        """
        Test check_valid_game_id_list correctly reject invalid input
        """
        valid_input_example = '1,2,3'
        invalid_input_example = '1sea,2;3'
        self.assertIsNotNone(cli_utility.check_valid_game_id_list(valid_input_example))
        self.assertIsNone(cli_utility.check_valid_game_id_list(invalid_input_example))
