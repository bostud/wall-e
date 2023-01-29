from typing import Optional

from core.db_models import Item
from core.db_models.session import create_autocommit_session
from core.use_cases.scheme import ItemData
from .read_record import get_item_db


def update_item_db(
    item_id: int,
    name: str,
    count: Optional[int] = None,
    description: Optional[str] = None,
) -> Optional[ItemData]:
    _update_data = {
        Item.name: name
    }
    if count is not None and count >= 0:
        _update_data[Item.count] = count

    if description is not None:
        _update_data[Item.description] = description

    with create_autocommit_session() as dbs:
        count = dbs.query(Item).filter(
            Item.item_id == item_id,
        ).update(_update_data)
        if count < 1:
            return None

    return get_item_db(item_id)
