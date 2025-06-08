from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiocache import Cache
from aiocache.serializers import PickleSerializer


class ThrottlingMiddleware(BaseMiddleware):
    """
    Middleware для ограничения частоты запросов (антифлуд)
    Использует in-memory кэш вместо Redis
    """

    def __init__(self):
        self.cache = Cache(
            Cache.MEMORY,  # Используем память
            serializer=PickleSerializer(),
            namespace="throttling"
        )

    async def __call__(self, handler, event: types.Message, data):
        user_id = event.from_user.id
        key = f"user:{user_id}"

        # Проверяем, не превышен ли лимит запросов
        is_throttled = await self.cache.get(key)
        if is_throttled:
            await event.answer("Слишком много запросов. Пожалуйста, подождите 2 секунды.")
            return

        # Устанавливаем временную блокировку
        await self.cache.set(key, True, ttl=2)  # Блокировка на 2 секунды

        # Пропускаем запрос дальше по цепочке middleware
        return await handler(event, data)