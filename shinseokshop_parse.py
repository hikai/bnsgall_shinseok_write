# -*- coding: utf-8 -*-
"""
Shinseok-shop parse without selenium.

@hikai
"""
from bs4 import BeautifulSoup
import requests


class Parser():
    """Parser."""

    def __init__(self):
        """
        Initalize method.

        self.url = Parse page url.
        self.soup = Parse object (BeautifulSoup object).
        """
        self.url = "http://bns.plaync.com/login/displayItemList?_=1485444240419"
        self.soup = BeautifulSoup(requests.get(self.url).text, "html.parser")
        self.soup = self.soup.select("div.boxThemeContents > ul.list \
                                            > li")

    def parse_data(self):
        """
        Parse data method.

        dict_item = Shinseok-shop item dictionary.
        dict_item: key = item name.
        dict_item: value = item price.
        """
        dict_item = {}
        for li in self.soup:
            name = li.select('a')[0].string
            shinseok = li.select("em")[0].string
            dict_item.update({name: shinseok})

        return dict_item


if __name__ == "__main__":
    parser = Parser()
    data = parser.parse_data()

    for k in data:
        print(k, data[k])
