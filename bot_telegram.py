from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import datetime
import os


key = "ee274a7924d788abb8dac7c9e00eb690"


def get_geocoding(city: str) -> dict:
    url_geocoding = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
    response_geocoding = requests.get(url=url_geocoding).json()[0]
    return {"lat": response_geocoding.get("lat"), "lon": response_geocoding.get("lon")}


def get_wheather(city: str) -> str:
    geocode = get_geocoding(city)
    lat = geocode.get("lat")
    lon = geocode.get("lon")
    url_weather = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&lang=ru&units=metric"
    response = requests.get(url=url_weather).json()
    return response


def get_response_for_telegram(obj: dict) -> None:
    list_weather = obj.get("list")
    city = obj.get("city").get("name")
    coord = obj.get("city").get("coord")

    sunrise = datetime.datetime.fromtimestamp(obj.get("city").get("sunrise"))
    sunset = datetime.datetime.fromtimestamp(obj.get("city").get("sunset"))
    during_day = sunset - sunrise

    for item in list_weather:
        time = datetime.datetime.fromtimestamp(item.get("dt"))
        main = item.get("main")
        temp = main.get("temp")
        pressure = main.get("pressure")
        sea_level = main.get("sea_level")
        humidity = main.get("humidity")
        description = item.get("weather")[0].get("description")
        icon = item.get("weather")[0].get("icon")
        wind_speed = item.get("wind").get("speed")
        wind_gust = item.get("wind").get("gust")
        repsonse = f"*** {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n" \
                         f"Погода в {city} на {time.strftime('%d-%m-%Y %H:%M')}\n" \
                         f"Описание: {description}" \
                         f"\nТемпература: {temp} градусов\n" \
                         f"Давление: {pressure} мм.рт.ст.\nУровень моря: {sea_level} м\n" \
                         f"Влажность: {humidity}%\nСкорость ветра: {wind_speed} м/с\nПорывы ветра: {wind_gust} м/с\n" \
                         f"Восход солнца: {sunrise.strftime('%H:%M')}\nЗаход солнца: {sunset.strftime('%H:%M')}\nПродолжительность дня: {during_day}\n" \
                   f"Широта: {coord.get('lat')}\nДолгота: {coord.get('lon')}"
        return repsonse


bot = Bot(token=os.getenv("TOKEN"))

dp = Dispatcher(bot)


@dp.message_handler()
async def function(message: types.Message):
    content = message.text
    await message.answer(get_data_from_db(content))


def get_data_from_db(message):
    raw_data = get_wheather(message)
    return get_response_for_telegram(raw_data)


executor.start_polling(dp, skip_updates=True)
