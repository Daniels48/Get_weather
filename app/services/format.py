from app.services.weather import WeatherService
from app.utils.format import format_weather


class WeatherResponseService:
    def __init__(self, weather_service: WeatherService) -> None:
        self.weather_service = weather_service

    async def get_weather_response(self, city: str) -> str:
        forecasts = await self.weather_service.get_forecast(city)

        if not forecasts:
            return "Не удалось получить прогноз погоды."

        return "\n\n──────────────\n\n".join(
            format_weather(forecast)
            for forecast in forecasts
        )