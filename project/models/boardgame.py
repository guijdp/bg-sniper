from project.models.base_entity import Base, BaseEntity
from sqlalchemy import Column, String


class Boardgame(BaseEntity, Base):
    __tablename__ = "boardgames"

    name = Column(String(130), unique=True)

    def __init__(self, name: str):
        self.name = name
