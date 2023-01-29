
from typing import Optional

from core.db_models import Item
from core.db_models.session import create_autocommit_session
from core.use_cases.scheme import ItemData
from .utils import prepare_item_data


def create_item_db(
    name: str,
    author_ip: str,
    count: Optional[int] = None,
    description: Optional[str] = None,
) -> ItemData:
    with create_autocommit_session() as dbs:
        item = Item(
            name=name,
            description=description,
            count=count,
            author_ip=author_ip,
        )
        dbs.add(item)
        dbs.flush()
        return prepare_item_data(item)
