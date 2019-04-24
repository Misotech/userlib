from band import logger, redis_factory
from typing import Dict
import ujson


def decode_dict(lst):
    """
    Convert list to pairs
    """
    for i in range(0, len(lst), 2):
        yield (* lst[i:i + 2], )


def encode_dict(dct: Dict):
    flat = []
    for k, v in dct.items():
        flat.append(k)
        flat.append(ujson.dumps(v))
    return flat


class Redis:
    def __init__(self, prefix=None):
        self.prefix = f'{prefix}:' if prefix else ''
        self.pool = None

    async def initialize(self):
        self.pool = await redis_factory.create_pool()

    async def unload(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    def _gen_key(self, key):
        return f'{self.prefix}{key}'

    def _check_ready(self):
        if self.pool:
            return True
        logger.warn('redis pool not ready')

    async def exists(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('EXISTS', key)

    async def get(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            stored = await conn.execute('GET', key)
            if stored:
                return stored.decode()

    async def incr(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            stored = await conn.execute('INCR', key)
            if stored:
                return stored

    async def set(self, key, val, ttl=None):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            if ttl:
                return await conn.execute('SETEX', key, ttl, val)
            else:
                return await conn.execute('SET', key, val)

    async def hset(self, key, field, val):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('HSET', key, field, val)

    async def hmset(self, key, *items):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('HMSET', key, *items)

    async def hget(self, key, field):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('HGET', key, field)

    def hmgetall(self, key):
        """
        DEPRECATED (WRONG)
        TODO: Remove when possible
        """
        return self.hgetall(key)

    async def hgetall(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            matches = await conn.execute('HGETALL', key)
            return [(
                k.decode(),
                v.decode(),
            ) for k, v in decode_dict(matches or [])]

    async def delete(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('DEL', key)

    async def increx(self, key, seconds):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            value = await conn.execute('INCR', key)
            if value:
                # if value == 1:
                await conn.execute('EXPIRE', key, seconds)
                return value

    async def expire(self, key, seconds):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('EXPIRE', key, seconds)

    async def ttl(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('TTL', key)


    async def sadd(self, key, val):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('SADD', key, val)


    async def smembers(self, key):
        if not self._check_ready():
            return
        with await self.pool as conn:
            key = self._gen_key(key)
            return await conn.execute('SMEMBERS', key)



def create_redis(*args, **kwargs) -> Redis:
    return Redis(*args, **kwargs)

