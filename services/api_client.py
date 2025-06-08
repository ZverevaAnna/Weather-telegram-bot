import aiohttp
from aiocache import cached, Cache
from aiocache.serializers import JsonSerializer
from config.settings import settings
from datetime import datetime


class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @cached(
        ttl=300,  # Кэшировать на 5 минут
        cache=Cache.MEMORY,  # Используем память
        serializer=JsonSerializer(),
        key_builder=lambda f, *args, **kwargs: f"weather:{args[1]}:{args[0]}"
    )
    async def get_weather(self, city: str, lang: str = "en"):
        """
        Получает данные о погоде с кэшированием в памяти
        :param city: Название города
        :param lang: Язык ответа (ru/en)
        :return: Данные о погоде в формате JSON
        """
        params = {
            "q": city,
            "appid": settings.OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": lang
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        self.BASE_URL,
                        params=params,
                        timeout=10
                ) as response:

                    if response.status == 200:
                        return await response.json()
                    else:
                        error_data = await response.json()
                        raise Exception(
                            f"Weather API error: {error_data.get('message', 'Unknown error')}"
                        )

            except aiohttp.ClientError as e:
                raise Exception(f"API request failed: {str(e)}")
            except asyncio.TimeoutError:
                raise Exception("API request timed out")