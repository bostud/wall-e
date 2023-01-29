from sqlalchemy import (
    Column,
    Integer,
    String,
)
from core.db_models.base import BaseModel


class Item(BaseModel):
    __tablename__ = 'item'

    item_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(String(50))
    description = Column(
        String(250),
        default=None,
        nullable=True,
    )
    count = Column(
        Integer,
        default=0,
    )
    author_ip = Column(
        String(25),
        default='',
    )
