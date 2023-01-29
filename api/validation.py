import math


def is_valid_crete_proto_input(item) -> bool:
    if len(item.name) > 50:
        return False
    if item.description and len(item.description) > 250:
        return False
    if int(item.items_count) > math.pow(2, 31):
        return False
    return True
