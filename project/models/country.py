from project.models.base_entity import Base, BaseEntity
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Country(BaseEntity, Base):
    __tablename__ = "countries"

    name = Column(String(130), unique=True)
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    currency = relationship("Currency", back_populates="countries")
    stores = relationship("Store", back_populates="country")

    def __init__(self, name: String):
        self.name = name
