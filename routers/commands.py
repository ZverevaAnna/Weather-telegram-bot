from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.inline import language_keyboard, main_menu_keyboard
from utils.formatters import get_message
from services.database import Database

router = Router()
db = Database()

@router.message(Command("start"))
async def cmd_start(message: Message):
    user = await db.get_user(message.from_user.id)
    if not user:
        await db.add_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            language="en"
        )
        await message.answer(
            get_message("welcome_new", "en"),
            reply_markup=language_keyboard("en")
        )
    else:
        await message.answer(
            get_message("welcome_back", user['language']).format(name=message.from_user.first_name),
            reply_markup=main_menu_keyboard(user['language'])
        )

@router.message(Command("help"))
async def cmd_help(message: Message):
    user = await db.get_user(message.from_user.id)
    lang = user['language'] if user else "en"
    await message.answer(get_message("help", lang))

@router.message(Command("weather"))
async def cmd_weather(message: Message):
    user = await db.get_user(message.from_user.id)
    lang = user['language'] if user else "en"
    await message.answer(get_message("ask_city", lang))

@router.message(Command("settings"))
async def cmd_settings(message: Message):
    user = await db.get_user(message.from_user.id)
    if user:
        await message.answer(
            get_message("settings_menu", user['language']),
            reply_markup=language_keyboard(user['language'])
        )
    else:
        await message.answer(get_message("not_registered", "en"))

@router.message(Command("history"))
async def cmd_history(message: Message):
    user = await db.get_user(message.from_user.id)
    if user:
        history = await db.get_weather_history(message.from_user.id)
        if history:
            response = get_message("history_header", user['language'])
            for item in history[:5]:  # Show last 5 requests
                response += f"\n{item['city']} - {item['timestamp']}"
            await message.answer(response)
        else:
            await message.answer(get_message("no_history", user['language']))
    else:
        await message.answer(get_message("not_registered", "en"))