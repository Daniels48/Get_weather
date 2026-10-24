from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message

from app.services.format import WeatherResponseService

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Привет! 🌦\n"
        "Отправь название города, чтобы узнать погоду."
    )




@router.message()
async def weather_handler(
    message: Message,
    weather_response_service: WeatherResponseService,
) -> None:
    if not message.text:
        return

    city = message.text.strip()

    if not city:
        await message.answer("Введи название города.")
        return

    try:
        response = await weather_response_service.get_weather_response(city)
    except ValueError as error:
        await message.answer(str(error))
        return

    await message.answer(
        text=response,
        parse_mode="HTML"
    )