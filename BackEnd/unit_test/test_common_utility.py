"""
Unit test file for common_utility.py
"""
from unittest import TestCase
from BackEnd.common_utility import check_positive


class TestCommonUtility(TestCase):
    """
    Class containing all test about common_utility.py
    """
    def test_check_positive(self):
        """
        Test function correctly identify positive float string
        """
        self.assertEqual(False, check_positive('Unable to be float'))
        self.assertEqual(False, check_positive('-1'))
        self.assertEqual(True, check_positive('1'))
        self.assertEqual(True, check_positive('01'))
        self.assertEqual(True, check_positive('1.0'))
