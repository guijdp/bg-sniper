import os
from logging import Logger

import requests
from lxml import etree
from project.blueprints.base_blueprint import BaseBlueprint
from project.session import DB

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class BoardGameGeek(BaseBlueprint):
    def __init__(self, session: DB, logger: Logger):
        super(BoardGameGeek, self).__init__(logger)
        self.session = session
        self.base_url = "https://boardgamegeek.com/browse/boardgame"
        self.next_page = 1
        self.init_total_pages()

    def init_total_pages(self):
        html_page = requests.get(self.base_url).text
        tree = etree.HTML(str(html_page))
        total_pages = (
            tree.xpath('//*[@id="maincontent"]/form/div/div[1]/a[6]/text()')[0]
            .replace("[", "")
            .replace("]", "")
        )
        self.total_pages = int(total_pages)

    def check_store(self):
        html_page = requests.get(f"{self.base_url}/page/{self.next_page}").text
        tree = etree.HTML(str(html_page))
        page_tree = tree.xpath('//*[@id="row_"]/td[3]')

        for game in page_tree:
            name = " ".join(game.xpath(".//div[2]/a/text()"))
            print(name)
            self.create_boardgame(name, None)

        self.next_page = 1 if self.next_page > self.total_pages else self.next_page + 1
