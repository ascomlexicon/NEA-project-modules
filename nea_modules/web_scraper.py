# Web Scraper Module
"""This module contains the WebScraper class, which is used to scrape data from the web."""
import requests
from bs4 import BeautifulSoup

class WebScraper:
    """This class is used to scrape data from the web."""
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.scrape()
    def scrape(self):
        """Scrapes the data from the web."""
        self.soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')
    def get_soup(self):
        """Returns the soup object."""
        return self.soup
    
