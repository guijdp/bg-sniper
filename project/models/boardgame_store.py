from sqlalchemy import Column, ForeignKey, Table

from models.base_entity import Base

boardgame_store = Table(
    "boardgame_store",
    Base.metadata,
    Column("store_id", ForeignKey("stores.id")),
    Column("boardgame_id", ForeignKey("boardgames.id")),
)
