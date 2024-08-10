import requests
from bs4 import BeautifulSoup

def get_laptops():
    url = 'https://www.sulpak.kg/f/noutbuki'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    laptops = []
    product_containers = soup.select('.product__item-inner')
    if not product_containers:
        print("No products found. Check the selectors.")
        return laptops

    for item in product_containers:
        title_element = item.select_one('.product__item-name a')
        price_element = item.select_one('.product__item-price')
        if title_element and price_element:
            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True).replace('сом', '').strip()
            laptops.append({
                'title': title,
                'price': price
            })

    return laptops

if __name__ == '__main__':
    laptops = get_laptops()
    if laptops:
        for laptop in laptops:
            print(f"{laptop['title']}\nЦена: {laptop['price']} сом\n")
    else:
        print("No laptops found.")
  
  
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = '7481976975:AAHZt2oe7M5G3FOMFeMSxeFaFN84IvUjfVY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


button_start = KeyboardButton('/start')
button_laptops = KeyboardButton('/laptops')


keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_markup.add(button_start, button_laptops)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для получения информации о ноутбуках с сайта Сулпак.", reply_markup=keyboard_markup)

@dp.message_handler(commands=['laptops'])
async def send_laptops(message: types.Message):
    laptops = get_laptops()
    if not laptops:
        await message.reply("Не удалось получить данные о ноутбуках.")
        return
    
    for laptop in laptops:
        await message.reply(f"{laptop['title']}\nЦена: {laptop['price']} сом", parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

