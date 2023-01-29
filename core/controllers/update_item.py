from typing import Optional

from core.controllers.cache import clean_cache
from core.use_cases.scheme import ItemData
from core.use_cases.update_record import update_item_db


def update_item(
    item_id: int,
    name: str,
    count: int = 1,
    description: Optional[str] = None,
) -> Optional[ItemData]:
    clean_cache(item_id=item_id)
    return update_item_db(item_id, name, count, description)
