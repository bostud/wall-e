import hashlib
from dataclasses import asdict
from dacite import from_dict
from typing import Optional, List
from core.cache_storage.storage import save_data, get_data, delete_data
from core.use_cases.scheme import ItemData


def create_data_key(**kwargs) -> str:
    _key = f"{'-'.join([f'{k}={v}' for k, v in kwargs.items()])}"
    return hashlib.sha256(_key.encode('utf-8')).hexdigest()


def get_cache_data(key: str) -> Optional[List[ItemData]]:
    data = get_data(key)
    if not data:
        return data
    return [from_dict(ItemData, d) for d in data]


def save_data_into_cache(
    key: str,
    data: List[ItemData],
):
    return save_data(key, [asdict(d) for d in data], 3600)


def clean_cache(**kwargs):
    return delete_data(create_data_key(**kwargs))
