from typing import Optional, List
from config import RECORDS_LIMIT, BASE_PAGE
from core.use_cases.read_record import (
    get_item_db,
    get_items_db,
)
from core.use_cases.scheme import ItemData
from core.controllers import cache


def get_items(
    limit: int = RECORDS_LIMIT,
    page: int = BASE_PAGE,
) -> List[ItemData]:
    return get_items_db(page=page, limit=limit)


def get_item(item_id: int) -> Optional[ItemData]:
    _key = cache.create_data_key(item_id=item_id)
    data = cache.get_cache_data(_key)
    if data:
        # returns list - select first
        data = data[0]
    else:
        data = get_item_db(item_id)
        if data:
            cache.save_data_into_cache(_key, [data])
    return data
