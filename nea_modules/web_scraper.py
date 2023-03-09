# Web Scraper Module
"""This module contains the WebScraper class, which is used to scrape data from the web."""

# Libraries
import requests
from typing import Any
from bs4 import BeautifulSoup

class WebScraper:
    """This class is used to scrape data from the web."""

    def __init__(self, url: str) -> None:
        """Initializes the WebScraper class."""

        self.__url: str = url
        self.__content: Any = None
        self.__soup: BeautifulSoup | None = None
        self.__html: str = ""
        self.__status_code: int = 0
        self.__tables: list[BeautifulSoup] = []

        self.get_request()

        if self.__status_code == 200:
            self.get_html()
        
        if self.__html:
            self.parse_html()

    def get_request(self) -> None:
        """This method sends a GET request to the url."""

        self.__content = requests.get(self.__url)
        self.__status_code = self.__content.status_code
    
    def get_html(self) -> None:
        """This method returns the html of the webpage."""

        self.__html = self.__content.text
    
    def parse_html(self) -> None:
        """This method parses the html of the webpage."""

        self.__soup = BeautifulSoup(self.__html, "html.parser")
        self.__tables = self.__soup.find_all("table")
    
    def get_tables(self) -> list[BeautifulSoup]:
        """This method returns the tables of the webpage."""

        return self.__tables

    def get_specific_table(self, table_index: int) -> BeautifulSoup:
        """This method returns the specific table of the webpage."""

        return self.__tables[table_index]

    def get_url(self) -> str:
        """This method returns the url."""

        return self.__url
    
    def get_status_code(self) -> int:
        """This method returns the status code."""

        return self.__status_code
