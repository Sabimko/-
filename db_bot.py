from aiogram import Bot, Dispatcher, types, executor
from confi import token
from logging import basicConfig, INFO
import sqlite3
import time

# from aiogram.dispatcher.storage import FSMContext


bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

connection = sqlite3.connect('user.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    username VARCHAR(100),
    phone_number text,
    cteated VARCHAR(100)
);
""")

@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?); ",
                   (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.contact.phone_number, time.ctime()))
    cursor.connection.commit()
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!")
    
# log = logging.info()
                         
executor.start_polling(dp, skip_updates=True)