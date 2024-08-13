from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import LabeledPrice, PreCheckoutQuery, CallbackQuery, BotCommand
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
import logging


bot = Bot(token='7481976975:AAHZt2oe7M5G3FOMFeMSxeFaFN84IvUjfVY')
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


buy_item_cb = CallbackData('buy', 'item_id')


LAPTOPS = {
    'laptop1': {'name': 'HP Victus', 'price': 7000000, 'photo_url': 'https://media.cnn.com/api/v1/images/stellar/prod/211025072623-macbook-pro-14-display-5.jpg?q=x_0,y_0,h_2268,w_4030,c_fill'},
    'laptop2': {'name': 'Dell XPS 13', 'price': 8000000, 'photo_url': 'https://lt2.pigugroup.eu/colours/606/072/28/60607228/dell-xps-13-plus-9320-black-c8e44_original.jpg'},
    'laptop3': {'name': 'MacBook Pro', 'price': 12000000, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTs8pKM_XLWZgUlKAvZtlcaNUAj2EZDcGZXqg&s'}
}


user_cart = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    for laptop_id, laptop in LAPTOPS.items():
        keyboard.add(InlineKeyboardButton(text=f"Купить {laptop['name']}",
                                          callback_data=buy_item_cb.new(item_id=laptop_id)))
    keyboard.add(InlineKeyboardButton(text="Перейти к оплате", callback_data="checkout"))
    await message.reply("Привет! Выберите ноутбук для покупки:", reply_markup=keyboard)

@dp.callback_query_handler(buy_item_cb.filter())
async def add_to_cart(callback: CallbackQuery, callback_data: dict):
    item_id = callback_data['item_id']
    user_id = callback.from_user.id
    
  
    if user_id not in user_cart:
        user_cart[user_id] = []

    user_cart[user_id].append(item_id)
    laptop = LAPTOPS[item_id]

    await callback.message.answer(f"Вы добавили {laptop['name']} в корзину.")
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "checkout")
async def checkout(callback: CallbackQuery):
    user_id = callback.from_user.id
    
    
    if user_id not in user_cart or not user_cart[user_id]:
        await callback.message.reply("Ваша корзина пуста. Добавьте товары перед оплатой.")
        return
    
    prices = []
    total_amount = 0
    for item_id in user_cart[user_id]:
        laptop = LAPTOPS[item_id]
        prices.append(LabeledPrice(label=laptop['name'], amount=laptop['price']))
        total_amount += laptop['price']

    
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Покупка ноутбуков',
        payload='multiple_laptops',
        description='Оплата выбранных ноутбуков',
        provider_token="1744374395:TEST:510fe05f8eac4398f49e",
        currency='RUB',
        prices=prices,
        start_parameter='multi_laptop_payment',
        photo_url=LAPTOPS[user_cart[user_id][0]]['photo_url'],
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    
    
    user_cart[user_id] = []
    await callback.answer()

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout(pre: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await message.reply("Спасибо за покупку! Ваш заказ был успешно оплачен.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
