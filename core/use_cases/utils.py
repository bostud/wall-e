from core.db_models import Item
from core.use_cases.scheme import ItemData


def prepare_item_data(item: Item) -> ItemData:
    return ItemData(
        item_id=item.item_id,
        name=item.name,
        description=item.description,
        items_count=item.count,
        author_ip=item.author_ip,
    )
