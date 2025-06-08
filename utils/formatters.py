import json
from pathlib import Path


def get_message(key: str, lang: str = "en"):
    locales_path = Path(__file__).parent.parent / "locales" / f"{lang}.json"
    with open(locales_path, "r", encoding="utf-8") as f:
        messages = json.load(f)
    return messages.get(key, key)


def format_weather_response(data: dict, lang: str) -> str:
    city = data['name']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    return get_message("weather_response", lang).format(
        city=city,
        temp=temp,
        feels_like=feels_like,
        humidity=humidity,
        wind_speed=wind_speed,
        description=description
    )