from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import LabeledPrice, PreCheckoutQuery,CallbackQuery, BotCommand
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from config import token, pay_token
import logging 

bot = Bot(token=token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

buy_laptop_cb = CallbackData('buy', 'item_id')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Купить ноутбук',
    callback_data=buy_laptop_cb.new(item_id = 'laptop')))
    await message.reply("Привет, выбери товар для покупки",
    reply_markup=keyboard)
    
@dp.callback_query_handler(buy_laptop_cb.filter(item_id = 'laptop'))
async def process_payment(callback:CallbackQuery):
    price = [LabeledPrice(label='hd victus', amount=7000000)]

    
    await bot.send_invoice(
        chat_id= callback.from_user.id,
        title='Ноутбук',
        payload='laptop',
        description= 'Ноутбук HP VICTUS 15-fa1093dx Intel Core i5-13420H(3.40-4.60GHz),8GB DDR4,512GB SSD m.2 NVMe,NVIDIA GTX 3050,15.6" FHD(1920x1080)144Hz IPS,WiFi ac,BT 5.0,HD WC,CR,DOS, Performance Blue',
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/c39/452_452_1d0e97ea46f4438969ab06dd5b311ca67/c390dfaee6c939a4a629a67caa60602a.jpg',
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    
    await callback.answer()
    
@dp.pre_checkout_query_handler(lambda query : True)
async def pre(pre : PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre.id, ok=True)
    
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def suc(message:types. Message):
    await message.reply("Спасибо что выбрали наш товар!")
    
executor.start_polling(dp,skip_updates=True)