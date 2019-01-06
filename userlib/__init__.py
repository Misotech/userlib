from .auth_store import AuthStoreRedis
from .redis import Redis

def create_redis(*args, **kwargs) -> Redis:
    return Redis(*args, **kwargs)
