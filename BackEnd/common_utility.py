"""This file is part of Tap Tap Scraper

Contain common useful function for other files
"""


def check_positive(value: str):
    """
    Check if given value is greater or equal to 0
    :param value: value in string
    :return: int(value)
    """
    try:
        return float(value) >= 0
    except ValueError:
        return False
