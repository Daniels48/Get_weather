from app.models.weathers import WeatherForecast


def format_weather(forecast: WeatherForecast) -> str:
    return (
        f"Погода в городе {forecast.city}\n"
        f"Дата: {forecast.forecast_time:%d.%m.%Y %H:%M}\n"
        f"Температура: {forecast.temperature:.1f} °C\n"
        f"Описание: {forecast.description}\n"
        f"Влажность: {forecast.humidity}%\n"
        f"Давление: {forecast.pressure} гПа\n"
        f"Ветер: {forecast.wind_speed:.1f} м/с"
    )