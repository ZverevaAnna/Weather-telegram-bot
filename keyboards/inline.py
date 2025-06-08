from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .builders import KeyboardBuilder
from utils.formatters import get_message

def language_keyboard(lang: str = "en") -> InlineKeyboardMarkup:
    """Клавиатура выбора языка"""
    buttons = [
        {"text": "English", "callback_data": "lang_en"},
        {"text": "Русский", "callback_data": "lang_ru"}
    ]
    return KeyboardBuilder.create(buttons, [2], lang).as_markup()

def main_menu_keyboard(lang: str = "en") -> InlineKeyboardMarkup:
    """Главное меню бота"""
    buttons = [
        {"text": "_weather_button", "callback_data": "get_weather"},
        {"text": "_history_button", "callback_data": "history"},
        {"text": "_settings_button", "callback_data": "settings"}
    ]
    return KeyboardBuilder.create(buttons, [1, 1, 1], lang).as_markup()