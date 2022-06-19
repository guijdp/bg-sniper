from project.models.base_entity import Base, BaseEntity
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Boardgame(BaseEntity, Base):
    __tablename__ = "boardgames"

    name = Column(String(130), unique=True)
    boardgame = relationship("Boardgame")
    facade_id = Column(Integer, ForeignKey("boardgames.id"))

    def __init__(self, name: str):
        self.name = name
