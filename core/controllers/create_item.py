from typing import Optional

from core.use_cases.create_record import create_item_db
from core.use_cases.scheme import ItemData


def create_item(
    author_ip: str,
    name: str,
    count: int = 1,
    description: Optional[str] = None,
) -> ItemData:
    return create_item_db(name, author_ip, count, description)
