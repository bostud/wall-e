from core.use_cases.delete_record import delete_item_db


def delete_item(item_id: int) -> bool:
    return delete_item_db(item_id)
