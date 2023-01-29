from core.db_models import Item
from core.db_models.session import create_autocommit_session


def delete_item_db(item_id: int) -> bool:
    with create_autocommit_session() as dbs:
        return dbs.query(Item).filter(
            Item.item_id == item_id
        ).delete() > 0
