import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseEntity(object):
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, onupdate=datetime.datetime.utcnow)

    def __init__(self, id: Integer, created: DateTime, modified: DateTime):
        self.id = (id,)
        self.created = (created,)
        self.modified = (modified,)
