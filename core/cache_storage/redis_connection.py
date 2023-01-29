import redis


from config import (
    REDIS_DB_NUM,
    REDIS_HOST,
    REDIS_PASS,
    REDIS_USER,
    REDIS_PORT,
)

redis_engine = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username=REDIS_USER,
    password=REDIS_PASS,
    db=REDIS_DB_NUM,
)
