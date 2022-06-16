from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.base_entity import Base, BaseEntity


class HistoricalPrice(BaseEntity, Base):
    __tablename__ = "historical_prices"

    price = Column(Float)
    boardgame_id = Column(Integer, ForeignKey("boardgames.id"))
    boardgames = relationship("Boardgame")

    def __init__(self, price: float):
        self.price = price
