from abc import ABC, abstractmethod
from typing import TypeVar

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

from models.base_entity import Base
from models.boardgame import Boardgame
from models.boardgame_store import boardgame_store
from models.country import Country
from models.currency import Currency
from models.historical_price import HistoricalPrice
from models.store import Store

T = TypeVar("T")


class DB(ABC):
    def __init__(self):
        """Constructor"""
        pass

    @abstractmethod
    def insert(self):
        """Commits transaction to database"""
        pass

    @abstractmethod
    def create_connection(self, connString):
        """Receives connection string and created connection"""
        pass

    @abstractmethod
    def create_session(self):
        """Creates session from connection"""
        pass

    @abstractmethod
    def create_session(self, tipo: T):
        """Creates session from connection"""
        pass

    @abstractmethod
    def insert(self):
        """Inserts desired data to database"""
        pass


class SQLiteSession(DB):
    def __init__(self):
        self.db = self.create_connection("sqlite:///sqlalchemy.sqlite")
        self.create_session()

    def create_connection(self, connString):
        self.engine = create_engine(connString, echo=True)
        Base.metadata.create_all(self.engine)

    def create_session(self):
        self.session = sessionmaker(bind=self.engine)()

    def insert(self, T):
        self.session.add(T)
        self.session.commit()

    def select(self, T):
        return self.session.execute(T)
