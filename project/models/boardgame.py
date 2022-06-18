from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from project.models.base_entity import Base, BaseEntity
from project.models.boardgame_store import boardgame_store
from project.models.store import Store


class Boardgame(BaseEntity, Base):
    __tablename__ = "boardgames"

    name = Column(String(130), unique=True)

    def __init__(self, name: str):
        self.name = name
