# Get Weather 🌦️

Get Weather — Telegram-бот на Python для получения информации о погоде в указанном городе.

## Возможности

- Получение погоды по названию города
- Обработка запросов пользователей через Telegram
- Интеграция с API погодного сервиса
- Вывод информации о погоде в удобном формате

## Технологии

- Python
- aiogram
- REST API
- Асинхронное программирование (`asyncio`)
- HTTP-запросы

## Запуск проекта

### 1. Клонирование репозитория

```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd Get_Weather
```

### 2. Создание виртуального окружения

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Создай файл `.env` на основе `.env.example`:

```bash
cp .env.example .env
```

Укажи токен Telegram-бота и API-ключ погодного сервиса, если он требуется используемым API.

### 5. Запуск бота

```bash
python bot.py
```

Название файла запуска (`bot.py`) необходимо заменить на фактическое, если точка входа в проект называется иначе.