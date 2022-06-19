from abc import ABC, abstractmethod
from typing import TypeVar

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.models.base_entity import Base
from project.models.boardgame import Boardgame
from project.models.boardgame_store import boardgame_store
from project.models.country import Country
from project.models.currency import Currency
from project.models.historical_price import HistoricalPrice
from project.models.store import Store

T = TypeVar("T")


class DB(ABC):

    def __init__(self):
        """Constructor"""
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
    def insert(self):
        """Commits transaction to database"""
        pass

    @abstractmethod
    def select(self, T):
        """Checks if entry exists"""
        pass

    def exists(self, T) -> bool:
        """Checks if entry exists"""
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
        try:
            self.session.add(T)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def select(self, T):
        return self.session.execute(T).first()

    def exists(self, T):
        return (self.session.query(T)).exists()
