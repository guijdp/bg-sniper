from logging import Logger

import requests
from lxml import etree
from project.blueprints.base_blueprint import BaseBlueprint
from project.session import DB


class FantazyWelt(BaseBlueprint):

    def __init__(self, session: DB, logger: Logger):
        super(FantazyWelt, self).__init__(logger)
        self.session = session
        self.base_url = "https://www.fantasywelt.de/Alle-deutschen-Brettspiele"
        self.country = "Germany"
        self.currency = "EUR"
        self.language = "de"
        self.store_name = "Fantazy Welt"
        self.next_page = 1
        self.init_total_pages()

    def init_total_pages(self):
        html_page = requests.get(self.base_url).text
        tree = etree.HTML(str(html_page))
        total_pages = (tree.xpath('//*[@id="paginations-select"]/a/text()')
                       [1].strip().split(" ")[1])
        self.total_pages = int(total_pages)

    def check_store(self):
        html_page = requests.get(f"{self.base_url}_s{self.next_page}").text
        tree = etree.HTML(str(html_page))
        page_tree = tree.xpath(
            '//*[@id="product-list"][1]//*[@class="product-wrapper col-xs-6 col-lg-4 col-xl-3"]'
        )

        currency = self.create_currency()
        language = self.create_language()

        country = self.create_country(currency)
        store = self.create_store(country)

        for game in page_tree:
            name = " ".join(
                game.xpath(".//*[@class='title']/a/text()")[0].split())
            price = (
                game.xpath(".//*[@class='price_wrapper']/strong/span/text()")
                [0].split(" ")[0].replace(",", "."))

            boardgame = self.create_boardgame(name)
            self.create_historical_price(price, boardgame, store, language)

        self.next_page = 1 if self.next_page > self.total_pages else self.next_page + 1
