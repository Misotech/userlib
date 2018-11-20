from band import logger, redis_factory


def pairs(l):
    """
    Convert list to pairs
    """
    for i in range(0, len(l), 2):
        # Create an index range for l of n items:
        yield (*l[i:i+2],)


class Redis:
    def __init__(self, prefix=None):
        self.prefix = f'{prefix}:' if prefix else ''
        self.pool = None

    async def initialize(self):
        self.pool = await redis_factory.create_pool()

    def gen_key(self, key):
        return f'{self.prefix}{key}'

    def check_ready(self):
        if self.pool:
            return True
        logger.warn('redis pool not ready')
        return False


    async def get(self, key):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            stored = await conn.execute('GET', key)
            if stored:
                return stored.decode()

    async def set(self, key, val, ttl=None):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            if ttl:
                return await conn.execute('SETEX', key, val, ttl)
            else:
                return await conn.execute('SET', key, val)

    async def hmset(self, key, *items):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            return await conn.execute('HMSET', key, *items)

    async def delete(self, key):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            return await conn.execute('DEL', key)

    async def increx(self, key, seconds):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            value = await conn.execute('INCR', key)
            if value:
                if value == 1:
                    await conn.execute('EXPIRE', key, seconds)
                return value

    async def expire(self, key, seconds):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            return await conn.execute('EXPIRE', key, seconds)

    async def hmgetall(self, key):
        if not self.check_ready():
            return
        with await self.pool as conn:
            key = self.gen_key(key)
            matches = await conn.execute('HGETALL', key)
            return [(
                k.decode(),
                v.decode(),
            ) for k, v in pairs(matches or [])]
