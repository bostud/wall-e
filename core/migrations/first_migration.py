from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP
from core.db_models.item import Item

from core.db_models.engine import engine


def run_up():
    meta = MetaData()
    Table(
        str(Item.__tablename__), meta,
        Column('item_id', Integer, primary_key=True, nullable=False,
               autoincrement=True),
        Column('name', String(50)),
        Column('description', String(250), default=None, nullable=True),
        Column('count', Integer, default=0),
        Column('author_ip', String(25), default=''),
        Column('create_time', TIMESTAMP, default=datetime.utcnow),
        Column('update_time', TIMESTAMP, onupdate=datetime.utcnow,
               default=None),
    )
    try:
        meta.create_all(engine)
    except Exception as e:
        print(e)
