import asyncio

from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN, OPENWEATHER_API_KEY
from app.router import router
from app.services.weather import OpenWeatherMapClient, WeatherService
from app.services.format import WeatherResponseService


async def main() -> None:
    weather_client = OpenWeatherMapClient(api_key=OPENWEATHER_API_KEY)

    weather_service = WeatherService(client=weather_client)

    weather_response_service = WeatherResponseService(weather_service=weather_service)

    dp = Dispatcher(weather_response_service=weather_response_service)

    dp.include_router(router)

    try:
        async with Bot(token=BOT_TOKEN) as bot:
            await dp.start_polling(bot)
    finally:
        await weather_client.close()


if __name__ == "__main__":
    asyncio.run(main())