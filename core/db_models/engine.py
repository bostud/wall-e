from sqlalchemy import create_engine
from config import (
    DB_HOST,
    DB_NAME,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
)


def get_db_url() -> str:
    return (
        f"postgresql://"
        f"{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )


engine = create_engine(get_db_url())
