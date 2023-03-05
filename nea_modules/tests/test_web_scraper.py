# Unit test for web scraper module
"""This module contains the unit tests for the web scraper module."""

import unittest
from nea_modules.web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    """This class contains the unit tests for the web scraper module."""
    def test_scrape(self):
        """Tests the scrape method."""
        scraper = WebScraper('https://www.google.com')
        self.assertIsNotNone(scraper.get_soup())

if __name__ == '__main__':
    unittest.main()