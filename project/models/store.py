from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from project.models.base_entity import Base, BaseEntity
from project.models.boardgame_store import boardgame_store


class Store(BaseEntity, Base):
    __tablename__ = "stores"

    name = Column(String(130), unique=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    country = relationship("Country", back_populates="stores")

    def __init__(self, name: str):
        self.name = name
