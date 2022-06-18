import requests
from lxml import etree
from sqlalchemy import desc
from sqlalchemy.sql import select

from project.models.boardgame import Boardgame
from project.models.historical_price import HistoricalPrice
from project.models.store import Store
from project.blueprints.base_blueprint import BaseBlueprint
from project.session import DB


class FantazyWelt(BaseBlueprint):
    def __init__(self, session: DB):
        self.session = session
        self.store_name = "Fantazy Welt"
        self.country = "Germany"
        self.currency = "EUR"
        self.base_url = "https://www.fantasywelt.de/Alle-deutschen-Brettspiele"
        self.next_page = 1
        self.init_total_pages()

    def init_total_pages(self):
        html_page = requests.get(self.base_url).text
        tree = etree.HTML(str(html_page))
        total_pages = (
            tree.xpath('//*[@id="paginations-select"]/a/text()')[1]
            .strip()
            .split(" ")[1]
        )
        self.total_pages = int(total_pages)

    def check_prices(self):
        html_page = requests.get(f"{self.base_url}_s{self.next_page}").text
        tree = etree.HTML(str(html_page))
        page_tree = tree.xpath(
            '//*[@id="product-list"][1]//*[@class="product-wrapper col-xs-6 col-lg-4 col-xl-3"]'
        )

        for game in page_tree:
            name = " ".join(game.xpath(".//*[@class='title']/a/text()")[0].split())
            price = (
                game.xpath(".//*[@class='price_wrapper']/strong/span/text()")[0]
                .split(" ")[0]
                .replace(",", ".")
            )

            store = self.create_store()
            boardgame = self.create_boardgame(name)
            self.create_historical_price(price, boardgame, store)

        self.next_page = 1 if self.next_page > self.total_pages else self.next_page + 1
