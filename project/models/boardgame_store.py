from project.models.base_entity import Base
from sqlalchemy import Column, ForeignKey, Table

boardgame_store = Table(
    "boardgame_store",
    Base.metadata,
    Column("store_id", ForeignKey("stores.id")),
    Column("boardgame_id", ForeignKey("boardgames.id")),
)
