from dataclasses import dataclass
from typing import Optional


@dataclass
class ItemData:
    item_id: int
    name: str
    items_count: int
    author_ip: str
    description: Optional[str] = None
