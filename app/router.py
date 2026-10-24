from aiogram import Router
from handlers.weather import router as router_weather

router = Router()

router.include_router(router_weather)