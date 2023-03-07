# Unit test for web scraper module
"""This module contains the unit tests for the web scraper module."""

# Libraries
import unittest
from nea_modules.web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    """This class contains the unit tests for the web scraper module."""

    def setUp(self) -> None:
        """This method sets up the test fixture before exercising it."""

        self.wikipedia_url = "https://en.wikipedia.org/wiki/Greenhouse_gas_emissions_by_country"
        self.scraper = WebScraper(self.wikipedia_url)
    
    def test_correct_url(self):
        """This method tests if the url is saved correctly."""

        self.assertEqual(self.scraper.get_url(), self.wikipedia_url)
    
    def test_status_code(self):
        """This method tests if the status code is correct."""

        self.assertEqual(self.scraper.get_status_code(), 200)
    
    def test_get_tables(self):
        """This method tests if the tables are retrieved correctly."""

        self.assertGreaterEqual(len(self.scraper.get_tables()), 1)
