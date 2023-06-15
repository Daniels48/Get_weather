@echo off

call %~dp0Avito_bot\venv\Scripts\activate

cd %~dp0Avito_bot

set TOKEN=5419112876:AAHXdNtEIvEegG962nkeyZS1Q0RfmyvjdDo

python bot_telegram.py

pause

