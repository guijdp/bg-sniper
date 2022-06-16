from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_entity import Base, BaseEntity
from models.boardgame_store import boardgame_store
from models.store import Store


class Boardgame(BaseEntity, Base):
    __tablename__ = "boardgames"

    name = Column(String(130))
    stores = relationship(
        Store.__name__,
        secondary=boardgame_store,
        back_populates=Store.__tablename__,
    )

    def __init__(self, name: str):
        self.name = name
