from api.json_scheme.scheme import Item
from core.use_cases.scheme import ItemData
from api.pb_scheme import scheme_pb2


def prepare_item_response(item_data: ItemData) -> Item:
    return Item(
        item_id=item_data.item_id,
        author_ip=item_data.author_ip,
        name=item_data.name,
        description=item_data.description,
        items_count=item_data.items_count,
    )


def prepare_item_proto(item_data: ItemData) -> scheme_pb2.Item:
    _pb_item = scheme_pb2.Item()

    _pb_item.name = item_data.name
    _pb_item.description = item_data.description or ''
    _pb_item.item_id = item_data.item_id
    _pb_item.items_count = item_data.items_count
    _pb_item.author_ip = item_data.author_ip

    return _pb_item
