from .auth_store import AuthStoreRedis
from .redis import Redis
from .clean import *


def create_redis(*args, **kwargs) -> Redis:
    return Redis(*args, **kwargs)

