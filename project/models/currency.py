from unicodedata import name

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from project.models.base_entity import Base, BaseEntity


class Currency(BaseEntity, Base):
    __tablename__ = "currencies"

    iso_code = Column(String(3), unique=True)
    countries = relationship("Country", back_populates="currency")

    def __init__(self, iso_code: String):
        self.iso_code = iso_code

    def to_string(self) -> str:
        return self.iso_code
