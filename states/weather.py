from aiogram.fsm.state import StatesGroup, State

class WeatherState(StatesGroup):
    waiting_for_city = State()