import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()


class Settings:
    # Токен бота Telegram (получается от @BotFather)
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # API ключ для OpenWeatherMap
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

    # Настройки базы данных
    class DB:
        # Используем SQLite по умолчанию
        NAME = os.getenv("DB_NAME", "weather_bot.db")


# Создаем экземпляр настроек
settings = Settings()