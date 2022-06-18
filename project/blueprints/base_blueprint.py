from abc import ABC, abstractmethod

from project.models.boardgame import Boardgame
from project.models.historical_price import HistoricalPrice
from project.models.store import Store
from project.session import DB
from sqlalchemy import desc
from sqlalchemy.sql import select


class BaseBlueprint(ABC):
    def __init__(self):
        """Constructor"""
        pass

    @abstractmethod
    def check_prices(self) -> None:
        """Checks page and returns"""
        pass

    def get_base_url(self):
        return self.base_url

    def get_total_pages(self):
        return self.total_pages

    def get_next_page(self):
        return self.next_page

    def create_store(self):
        store = self.session.select(select(Store).where(Store.name == self.store_name))

        if store is None:
            store = Store(self.store_name)
            self.session.insert(store)
        else:
            store = store[0]

        return store

    def create_boardgame(self, name):
        boardgame = self.session.select(select(Boardgame).where(Boardgame.name == name))
        if boardgame is None:
            boardgame = Boardgame(name)
            self.session.insert(boardgame)
        else:
            boardgame = boardgame[0]

        return boardgame

    def create_historical_price(self, price, boardgame, store):
        old_price = self.session.select(
            select(HistoricalPrice)
            .where(
                HistoricalPrice.boardgame_id == boardgame.id
                and HistoricalPrice.store_id == store.id
            )
            .order_by(desc(HistoricalPrice.created))
        )

        if old_price is None or old_price[0].price != float(price):
            historical_price = HistoricalPrice(price)
            historical_price.boardgame = boardgame
            historical_price.store = store
            self.session.insert(historical_price)
