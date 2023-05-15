from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from re import findall, search
import os


def get_params(bs4_obj):
    bs4_content = list(list(bs4_obj.children)[2].children)
    obj = {}
    body = list(bs4_content[1].children)
    slider = bs4_content[0]
    obj["image"] = search(r"https://[^\s\"\']+", string=str(slider)).group(0)
    name_item = "iva-item-"
    for item in body[::-1]:
        string = str(item)
        if findall(r"data-marker=[\"\']item-line[\"\']", string):
            obj["agent"] = item.text
        if findall(f"{name_item}description", string):
            obj["description"] = item.text
        if findall(f"{name_item}developmentNameStep", string):
            obj["address"] = item.text
        if findall(f"{name_item}autoParamsStep", string):
            obj["conditions"] = item.text
        if findall(f"{name_item}dateInfoStep", string):
            obj["time"] = item.text
        if findall(f"{name_item}titleStep", string):
            obj["rooms"] = item.text
        if findall(f"{name_item}priceStep", string):
            obj["price"] = item.text
    return obj


driver = webdriver.Chrome(executable_path="./chrome/chromedriver.exe")
url = "https://www.avito.ru/anapa/kvartiry/sdam/na_dlitelnyy_srok"
try:
    driver.get(url=url)
    list_elements = driver.find_elements(By.CSS_SELECTOR, value='[data-marker="item"]')
    with open("./page.html", mode="w+", encoding="utf-8") as file:
        for elem in list_elements:
            file.write(f"<div class='item'> {elem.get_property('innerHTML')} </div>")

        soup_obj = BeautifulSoup(file.read(), "html.parser")
        list_children = list(soup_obj.children)
        obj = []

        for items in list_children:
            params = get_params(items)
            print(params)

except Exception as c:
    print(c)
finally:
    driver.close()
    driver.quit()


bot = Bot(token=os.getenv("TOKEN"))

dp = Dispatcher(bot)

@dp.message_handler()
async def function(message: types.Message):
    content = message.text
    await message.answer(get_data_from_db(content))


def get_data_from_db(message):
    list_city = {"анапа": "anapa", "иваново": "ivanovo"}



executor.start_polling(dp, skip_updates=True)
