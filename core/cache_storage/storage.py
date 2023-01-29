import json
from typing import Optional

from config import REDIS_KEY_PREFIX
from core.cache_storage.redis_connection import redis_engine


def _prepare_key(key: str) -> str:
    return f"{REDIS_KEY_PREFIX}:{key}"


def save_data(key: str, data: list, ttl: int = -1) -> None:
    if ttl < 0:
        ttl = None

    redis_engine.set(_prepare_key(key), json.dumps(data), ttl)


def get_data(key: str) -> Optional[dict]:
    data = redis_engine.get(_prepare_key(key))
    if not data:
        return None
    return json.loads(data)


def delete_data(key: str) -> None:
    return redis_engine.delete(_prepare_key(key))
