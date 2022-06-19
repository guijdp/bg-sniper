import inspect
from abc import ABC, abstractmethod
from asyncio.log import logger
from logging import Logger

from project.models.boardgame import Boardgame
from project.models.country import Country
from project.models.currency import Currency
from project.models.historical_price import HistoricalPrice
from project.models.language import Language
from project.models.store import Store
from sqlalchemy import desc, exc, inspect
from sqlalchemy.sql import select


class BaseBlueprint(ABC):

    def __init__(self, logger: Logger):
        self.logger = logger

    @abstractmethod
    def check_store(self) -> None:
        """Checks page and returns"""
        pass

    def get_base_url(self) -> str:
        return self.base_url

    def get_total_pages(self) -> int:
        return self.total_pages

    def get_next_page(self) -> int:
        return self.next_page

    def create_language(self) -> None:
        language = Language(self.language)

        try:
            self.session.insert(language)
            return language

        except exc.IntegrityError as e:
            self.logger.debug(
                f"Could not insert language: {self.language}, Reason: {e.args[0]}"
            )

        except Exception as e:
            self.logger.error(
                f"Could not insert language: {self.language}, Reason: {e.args[0]}"
            )

        return self.session.select(
            select(Language).where(Language.name == self.language))[0]

    def create_currency(self):
        currency = Currency(self.currency)

        try:
            self.session.insert(currency)
            return currency

        except exc.IntegrityError as e:
            self.logger.debug(
                f"Could not insert currency: {self.currency}, Reason: {e.args[0]}"
            )

        except Exception as e:
            self.logger.error(
                f"Could not insert currency: {self.currency}, Reason: {e.args[0]}"
            )

        return self.session.select(
            select(Currency).where(Currency.iso_code == self.currency))[0]

    def create_country(self, currency):
        country = Country(self.country)
        country.currency = currency

        try:
            self.session.insert(country)
            return country

        except exc.IntegrityError as e:
            self.logger.debug(
                f"Could not insert country: {self.country}, Reason: {e.args[0]}"
            )

        except Exception as e:
            self.logger.error(
                f"Could not insert country: {self.country}, Reason: {e.args[0]}"
            )

        return self.session.select(
            select(Country).where(Country.name == self.country))[0]

    def create_store(self, country):
        store = store(self.store_name)
        store.country = country

        try:
            self.session.insert(store)
            return store

        except exc.IntegrityError as e:
            self.logger.debug(
                f"Could not insert store: {self.store_name}, Reason: {e.args[0]}"
            )

        except Exception as e:
            self.logger.error(
                f"Could not insert store: {self.store_name}, Reason: {e.args[0]}"
            )

        return self.session.select(
            select(Store).where(Store.name == self.store_name))[0]

    def create_boardgame(self, name, facade_id):
        boardgame = Boardgame(name)
        boardgame.facade_id = facade_id

        try:
            self.session.insert(boardgame)
            return boardgame

        except exc.IntegrityError as e:
            self.logger.debug(
                f"Could not insert boardgame: {name}, Reason: {e.args[0]}")

        except Exception as e:
            self.logger.error(
                f"Could not insert boardgame: {name}, Reason: {e.args[0]}")

        return self.session.select(
            select(Boardgame).where(Boardgame.name == name))[0]

    def create_historical_price(self, price, boardgame, store, language):
        old_price = self.session.select(
            select(HistoricalPrice).where(
                HistoricalPrice.boardgame_id == boardgame.id
                and HistoricalPrice.store_id == store.id
                and HistoricalPrice.language_id == language.id).order_by(
                    desc(HistoricalPrice.created)))

        if old_price is None or old_price[0].price != float(price):
            historical_price = HistoricalPrice(price)
            historical_price.boardgame = boardgame
            historical_price.store = store
            historical_price.language = language
            self.session.insert(historical_price)
