from .redis import Redis


def create_redis(*args, **kwargs):
    return Redis(*args, **kwargs)
