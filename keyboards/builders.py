from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List, Dict, Optional
from utils.formatters import get_message


class KeyboardBuilder:
    """Основной класс для построения клавиатур"""

    @staticmethod
    def create(
            buttons: List[Dict[str, str]],
            adjust: Optional[List[int]] = None,
            lang: str = "en"
    ) -> InlineKeyboardBuilder:
        """
        Универсальный метод создания клавиатур
        :param buttons: [{"text": "Текст или ключ перевода", "callback_data": "data"}]
        :param adjust: Схема расположения [2, 1] - 2 кнопки в первом ряду, 1 во втором
        :param lang: Язык для локализации
        """
        builder = InlineKeyboardBuilder()

        for btn in buttons:
            text = get_message(btn["text"], lang) if btn["text"].startswith("_") else btn["text"]
            builder.button(text=text, callback_data=btn["callback_data"])

        if adjust:
            builder.adjust(*adjust)

        return builder