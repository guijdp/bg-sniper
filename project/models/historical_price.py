from project.models.base_entity import Base, BaseEntity
from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


class HistoricalPrice(BaseEntity, Base):
    __tablename__ = "historical_prices"

    price = Column(Float)
    boardgame_id = Column(Integer, ForeignKey("boardgames.id"))
    boardgame = relationship("Boardgame")
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store")
    language = relationship("Language")
    language_id = Column(Integer, ForeignKey("languages.id"))

    def __init__(self, price: float):
        self.price = price
