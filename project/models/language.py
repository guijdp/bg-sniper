from project.models.base_entity import Base, BaseEntity
from sqlalchemy import Column, String


class Language(BaseEntity, Base):
    __tablename__ = "languages"

    name = Column(String(5))

    def __init__(self, name: String):
        self.name = name
