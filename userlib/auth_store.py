import ujson

class AuthStoreRedis:
    def __init__(self, redis, key):
        self.redis = redis
        self.key = key

    async def set(self, data):
        await self.redis.set(self.key, ujson.dumps(data))

    async def get(self):
        data = await self.redis.get(self.key)
        if data:
            return ujson.loads(data)

    async def delete(self):
        await self.redis.delete(self.key)

