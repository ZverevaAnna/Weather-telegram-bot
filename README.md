# WhatEverWeather Bot 

Телеграм-бот с поддержкой нескольких языков, предоставляющий актуальную информацию о погоде в любом городе мира 

## Автор: 
Зверева Анна Дмитриевна (335068)  

## Возможности бота

- Получение погоды для любого города
- Переключение между английским и русским языками
- История запросов погоды
- Кэширование запросов для быстрой работы
- Ограничение запросов для защиты от злоупотреблений

## Требования

- Python 3.9+
- Токен Telegram бота
- API ключ OpenWeatherMap

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ZverevaAnna/whateverweather-bot.git
cd whateverweather-bot
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
# Активация:
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корне проекта и добавьте:
```ini
BOT_TOKEN=ваш_токен_бота
OPENWEATHER_API_KEY=ваш_api_ключ
```

## Как получить API ключи

1. **Токен Telegram бота**:
   - Напишите [@BotFather](https://t.me/BotFather) в Telegram
   - Используйте команду `/newbot` для создания бота и следуйте инструкции в боте
   - Скопируйте токен, который предоставит BotFather

2. **API ключ OpenWeatherMap**:
   - Зарегистрируйтесь на [OpenWeatherMap](https://openweathermap.org/api)
   - В аккаунте найдите вкладку "API Keys"
   - Создайте новый ключ или используйте существующий
   - OpenWeatherMap требует 10-15 минут для активации нового ключа

## Запуск бота

```bash
python bot.py
```

## Команды бота

- `/start` - Начать работу с ботом
- `/help` - Помощь по использованию бота
- `/weather` - Узнать погоду в городе
- `/settings` - Настройки бота
- `/history` - История ваших запросов
