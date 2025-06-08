from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.weather import WeatherState
from services.api_client import WeatherAPI
from services.database import Database
from utils.formatters import get_message, format_weather_response
from keyboards.inline import main_menu_keyboard, language_keyboard

router = Router()
weather_api = WeatherAPI()
db = Database()

@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    await db.update_user(callback.from_user.id, {"language": lang})
    await callback.message.edit_text(
        get_message("language_set", lang),
        reply_markup=main_menu_keyboard(lang)
    )

@router.callback_query(F.data == "get_weather")
async def get_weather_callback(callback: CallbackQuery, state: FSMContext):
    user = await db.get_user(callback.from_user.id)
    await callback.message.answer(get_message("ask_city", user['language']))
    await state.set_state(WeatherState.waiting_for_city)

@router.callback_query(F.data == "history")
async def history_callback(callback: CallbackQuery):
    user = await db.get_user(callback.from_user.id)
    history = await db.get_weather_history(callback.from_user.id)
    if history:
        response = get_message("history_header", user['language'])
        for item in history[:5]:
            response += f"\n{item['city']} - {item['timestamp']}"
        await callback.message.answer(response)
    else:
        await callback.message.answer(get_message("no_history", user['language']))

@router.callback_query(F.data == "settings")
async def settings_callback(callback: CallbackQuery):
    user = await db.get_user(callback.from_user.id)
    await callback.message.answer(
        get_message("settings_menu", user['language']),
        reply_markup=language_keyboard(user['language'])
    )