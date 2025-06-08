from aiogram import Router
from .weather import router as weather_router

router = Router()
router.include_router(weather_router)

__all__ = ['router']