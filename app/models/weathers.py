from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class WeatherForecast:
    city: str
    forecast_time: datetime
    temperature: float
    description: str
    pressure: int
    humidity: int
    wind_speed: float
    wind_gust: float | None
    sunrise: datetime
    sunset: datetime
    latitude: float
    longitude: float