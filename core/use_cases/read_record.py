from typing import Optional, List

from core.db_models import Item
from core.db_models.session import create_db_session
from core.use_cases.scheme import ItemData
from .utils import prepare_item_data


def get_item_db(item_id: int) -> Optional[ItemData]:
    dbs = create_db_session()
    record = dbs.query(Item).filter(
        Item.item_id == item_id,
    ).first()
    if not record:
        return None
    return prepare_item_data(record)


def get_items_db(
    page: int,
    limit: int,
) -> Optional[List[ItemData]]:
    dbs = create_db_session()
    query = dbs.query(Item).offset(
        (page - 1) * limit
    ).limit(limit)

    return [prepare_item_data(record) for record in query.all()]
