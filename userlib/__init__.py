from .redis import Redis
from .auth_store import AuthStoreRedis


def create_redis(*args, **kwargs) -> Redis:
    return Redis(*args, **kwargs)
