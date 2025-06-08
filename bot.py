import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from config.settings import settings
from routers import commands_router, callback_router, handlers_router
from middlewares.throttling import ThrottlingMiddleware
from utils.logger import setup_logger


async def main():
    setup_logger()
    storage = MemoryStorage()
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=storage)

    dp.message.middleware(ThrottlingMiddleware())

    dp.include_router(commands_router)
    dp.include_router(callback_router)
    dp.include_router(handlers_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())