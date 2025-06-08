from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.weather import WeatherState
from services.api_client import WeatherAPI
from services.database import Database
from utils.formatters import get_message, format_weather_response
from keyboards.inline import main_menu_keyboard

router = Router()
weather_api = WeatherAPI()
db = Database()


@router.message(WeatherState.waiting_for_city, F.text)
async def process_city(message: Message, state: FSMContext):
    user = await db.get_user(message.from_user.id)
    try:
        weather_data = await weather_api.get_weather(message.text, user['language'])
        formatted_response = format_weather_response(weather_data, user['language'])

        await db.add_weather_request(
            user_id=message.from_user.id,
            city=message.text,
            weather_data=formatted_response
        )

        await message.answer(
            formatted_response,
            reply_markup=main_menu_keyboard(user['language'])
        )
    except Exception as e:
        await message.answer(
            get_message("weather_error", user['language']),
            reply_markup=main_menu_keyboard(user['language'])
        )
    finally:
        await state.clear()


__all__ = ['router']