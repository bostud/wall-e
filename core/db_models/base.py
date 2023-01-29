from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, TIMESTAMP
from datetime import datetime


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    create_time = Column(
        TIMESTAMP,
        default=datetime.utcnow,
    )
    update_time = Column(
        TIMESTAMP,
        onupdate=datetime.utcnow,
        default=None,
    )
