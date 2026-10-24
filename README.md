# Get Weather 

Get Weather — Telegram-бот на Python для получения прогноза погоды по названию города. Использует OpenWeatherMap API для получения метеорологических данных и aiogram для взаимодействия с Telegram.

## Возможности

- Получение погоды по названию города
- Интеграция с API погодного сервиса
- Вывод информации о погоде в удобном формате

## Технологии

- Python
- aiogram
- OpenWeatherMap API
- httpx
- Docker

## Запуск проекта

### 1️⃣ Клонировать репозиторий

```bash
git clone https://github.com/Daniels48/Get_Weather.git
```
```bash
cd Get_Weather
```

### 2️⃣ Создать файл `.env`

Скопируйте `.env.example` и переименуйте его в `.env`:

```bash
cp .env.example .env
```

Укажи в .env необходимые значения:

```bash
TOKEN=your_telegram_bot_token
OPENWEATHER_API_KEY=your_openweathermap_api_key
```

### 3️⃣ Запустить контейнеры

```bash
docker compose up -d --build
```