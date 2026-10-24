from datetime import datetime, timedelta, timezone
import httpx

from app.models.weathers import WeatherForecast


class OpenWeatherMapClient:
    BASE_URL = "https://api.openweathermap.org"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.client = httpx.AsyncClient(base_url=self.BASE_URL,timeout=10.0,)

    async def get_coordinates(self, city: str) -> dict:
        response = await self.client.get(
            "/geo/1.0/direct",
            params={"q": city,"appid": self.api_key,"limit": 1},
        )
        response.raise_for_status()

        data = response.json()

        if not data:
            raise ValueError(f"Город «{city}» не найден.")

        return data[0]

    async def get_forecast(self, latitude: float, longitude: float) -> dict:
        response = await self.client.get(
            "/data/2.5/forecast",
            params={
                "lat": latitude,
                "lon": longitude,
                "appid": self.api_key,
                "lang": "ru",
                "units": "metric",
            },
        )
        response.raise_for_status()

        return response.json()

    async def close(self) -> None:
        await self.client.aclose()


class WeatherService:
    def __init__(self, client: OpenWeatherMapClient) -> None:
        self.client = client

    async def get_forecast(
        self,
        city: str,
    ) -> list[WeatherForecast]:
        coordinates = await self.client.get_coordinates(city)

        latitude = coordinates["lat"]
        longitude = coordinates["lon"]

        response = await self.client.get_forecast(
            latitude=latitude,
            longitude=longitude,
        )

        city_data = response["city"]

        city_timezone = timezone(
            timedelta(seconds=city_data.get("timezone", 0))
        )

        sunrise = datetime.fromtimestamp(
            city_data["sunrise"],
            tz=city_timezone,
        )
        sunset = datetime.fromtimestamp(
            city_data["sunset"],
            tz=city_timezone,
        )

        forecasts: list[WeatherForecast] = []

        for item in response.get("list", [])[:8]:
            main = item["main"]
            weather = item["weather"][0]
            wind = item.get("wind", {})

            forecasts.append(
                WeatherForecast(
                    city=city_data["name"],
                    forecast_time=datetime.fromtimestamp(
                        item["dt"],
                        tz=city_timezone,
                    ),
                    temperature=main["temp"],
                    description=weather["description"],
                    pressure=main["pressure"],
                    humidity=main["humidity"],
                    wind_speed=wind.get("speed", 0),
                    wind_gust=wind.get("gust"),
                    sunrise=sunrise,
                    sunset=sunset,
                    latitude=latitude,
                    longitude=longitude,
                )
            )

        return forecasts
#
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# import requests
# import datetime
# import os
#
#
# key =
#
#
# def get_geocoding(city: str) -> dict:
#     url_geocoding = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
#     response_geocoding = requests.get(url=url_geocoding).json()[0]
#     return {"lat": response_geocoding.get("lat"), "lon": response_geocoding.get("lon")}
#
#
# def get_wheather(city: str) -> str:
#     geocode = get_geocoding(city)
#     lat = geocode.get("lat")
#     lon = geocode.get("lon")
#     url_weather = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&lang=ru&units=metric"
#     response = requests.get(url=url_weather).json()
#     return response
#
#
# def get_response_for_telegram(obj: dict) -> None:
#     list_weather = obj.get("list")
#     city = obj.get("city").get("name")
#     coord = obj.get("city").get("coord")
#
#     sunrise = datetime.datetime.fromtimestamp(obj.get("city").get("sunrise"))
#     sunset = datetime.datetime.fromtimestamp(obj.get("city").get("sunset"))
#     during_day = sunset - sunrise
#
#     for item in list_weather:
#         time = datetime.datetime.fromtimestamp(item.get("dt"))
#         main = item.get("main")
#         temp = main.get("temp")
#         pressure = main.get("pressure")
#         sea_level = main.get("sea_level")
#         humidity = main.get("humidity")
#         description = item.get("weather")[0].get("description")
#         icon = item.get("weather")[0].get("icon")
#         wind_speed = item.get("wind").get("speed")
#         wind_gust = item.get("wind").get("gust")
#         repsonse = f"*** {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n" \
#                          f"Погода в {city} на {time.strftime('%d-%m-%Y %H:%M')}\n" \
#                          f"Описание: {description}" \
#                          f"\nТемпература: {temp} градусов\n" \
#                          f"Давление: {pressure} мм.рт.ст.\nУровень моря: {sea_level} м\n" \
#                          f"Влажность: {humidity}%\nСкорость ветра: {wind_speed} м/с\nПорывы ветра: {wind_gust} м/с\n" \
#                          f"Восход солнца: {sunrise.strftime('%H:%M')}\nЗаход солнца: {sunset.strftime('%H:%M')}\nПродолжительность дня: {during_day}\n" \
#                    f"Широта: {coord.get('lat')}\nДолгота: {coord.get('lon')}"
#         return repsonse
#
#
# bot = Bot(token=os.getenv("TOKEN"))
#
# dp = Dispatcher(bot)
#
#
# @dp.message_handler()
# async def function(message: types.Message):
#     content = message.text
#     await message.answer(get_data_from_db(content))
#
#
# def get_data_from_db(message):
#     raw_data = get_wheather(message)
#     return get_response_for_telegram(raw_data)
#
#
# executor.start_polling(dp, skip_updates=True)
