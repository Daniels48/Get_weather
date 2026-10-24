from aiogram import Router
from app.handlers.weather import router as router_weather

router = Router()

router.include_router(router_weather)