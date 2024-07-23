# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, types, executor
from confi import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О Нас'),
    types.KeyboardButton('Товары'),
    types.KeyboardButton('Заказать'),
    types.KeyboardButton('Контакты')
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about_us(message: types.Message):
    await message.reply("Магазин бытовой техники «TechnoShop».Наша миссия – сегодня обеспечить всех соотечественников самыми доступными и качественными продуктами. Все наше внимание сосредоточено на введении срочных платежей как халяльной нации, основанной на подходе легкой покупки оборудования.")


products = [
    types.KeyboardButton("Смартфоны"),
    types.KeyboardButton("Кондиционеры"),
    types.KeyboardButton("Ноутбуки"),
    types.KeyboardButton("Телевизоры"),  
    types.KeyboardButton("Аксесуары со скидкой"),
    types.KeyboardButton("Заказать"),
    types.KeyboardButton("Назад")    
]

products_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*products)

@dp.message_handler(text='Товары')
async def show_products(message: types.Message):
    await message.answer("Вот наши товары: ", reply_markup=products_keyboard)


@dp.message_handler(text='Смартфоны')
async def show_smartphones(message: types.Message):
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/06/bfyluw3tkbnxthji79guwsz9fvjihkvac6ml3tm4.jpg",
        caption=(
            "Смартфон Apple iPhone 15 Pro 128ГБ Dual, серый\n"
            "Артикул: 123456\n"
            "Цена: 1000 USD\n"
            "Информация: Смартфон Apple iPhone 15 Pro 128ГБ Dual, серый"
        )
    )

    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/07/new-project-9-6-14-10-3-1.jpg",
        caption=(
            "Мобильный телефон iPhone 14 Pro Max 128GB Deep Purple\n"
            "Артикул: 789012\n"
            "Цена: 900 USD\n"
            "Информация: Мобильный телефон iPhone 14 Pro Max 128GB Deep Purple"
        )
    )
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/06/new-project-9-4.jpg",
        caption=(
            "Мобильный телефон Xiaomi Redmi Note 13 Pro+ 5G, Midnight Black, 8/256 GB\n"
            "Артикул: 243332\n"
            "Цена: 760 USD\n"
            "Информация: Xiaomi Redmi Note 13 Pro+ 5G, Midnight Black, 8/256 GB"
        )
    )

    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/07/new-project-9-6-14-7.jpg",
        caption=(
            "Мобильный телефон Мобильный телефон Samsung A25 (A256) 6/128 Blue Black\n"
            "Артикул: 43789012\n"
            "Цена: 950 USD\n"
            "Информация: Мобильный телефон Samsung A25 (A256) 6/128 Blue Black"
        )
    )
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/06/radmi-note-13-pro.jpg",
        caption=(
            "Мобильный телефон Мобильный телефон Redmi Note 13 Pro 8/256GB Midnight Black\n"
            "Артикул: 7234012\n"
            "Цена: 600 USD\n"
            "Информация: Мобильный телефон Redmi Note 13 Pro 8/256GB Midnight Black"
        )
    )


@dp.message_handler(text='Кондиционеры')
async def show_air_conditioners(message: types.Message):
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/06/artel-1-1.jpg",
        caption=(
            "Кондиционер Artel ARTSID2CW12BE Iceberg Invertor, белый"
            "Артикул: 36544012\n"
            "Цена: 1200 USD\n"
            "Информация: Кондиционер Artel ARTSID2CW12BE Iceberg Invertor, белый"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/06/artel-3.jpg", 
        caption=(
            "Кондиционер Artel Shahrisabz-S Inverter SIR1W12BE, белый"
            "Артикул: 4404712\n"
            "Цена: 1000 USD\n"
            "Информация: Кондиционер Artel Shahrisabz-S Inverter SIR1W12BE, белый"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/07/b1196657-9a9b-4e14-9394-f766387ca76c.jpg",
        caption=(
            "Кондиционер Avalon 18 Inverter AVL-AC18R32 DC Full"
            "Артикул: 854404712\n"
            "Цена: 1500 USD\n"
            "Информация: Кондиционер Avalon 18 Inverter AVL-AC18R32 DC Full"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/07/b1196657-9a9b-4e14-9394-f766387ca76c.jpg",
        caption=(
            "Кондиционер Avalon 24 Inverter AVL-AC24R32 DC Full"
            "Артикул: 0654404712\n"
            "Цена: 1000 USD\n"
            "Информация: Кондиционер Avalon 24 Inverter AVL-AC24R32 DC Full"
            ))

@dp.message_handler(text='Ноутбуки')
async def show_laptops(message:types.Message):
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/04/viktus-1.png",
        caption=(
            " Ноутбук: HP VICTUS 15-fa1093dx (15,6 ” FHD IPS 144 GHz | i5-13420h | DDR4 8 GB | SSD 512 GB | RTX 3050 6 GB)"
            "Артикул: 464404712\n"
            "Цена: 2000 USD\n"
            "Информация: Ноутбук: HP VICTUS 15-fa1093dx (15,6 ” FHD IPS 144 GHz | i5-13420h | DDR4 8 GB | SSD 512 GB | RTX 3050 6 GB)"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/03/noutbuk-asus-expertbook-b1502cba-bq0561-1.png",
        caption=(
            "Ноутбук Asus ExpertBook (B1502CBA-BQ0561) / i5-1235U / 8GB / SSD 512GB / 15.6″, синий"
            "Артикул: 1574404712\n"
            "Цена: 2500 USD\n"
            "Информация: Ноутбук Asus ExpertBook (B1502CBA-BQ0561) / i5-1235U / 8GB / SSD 512GB / 15.6″, синий"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/03/noutbuk-hp-envy-x360-14-es0033dx-4.png",
        caption=(
            "Ноутбук HP ENVY x360 14-ES0013DX (7H9Y4UA) / i5-1335U / 8GB / SSD 512GB / 14″, серебристый"
            "Артикул: 9064404712\n"
            "Цена: 1700 USD\n"
            "Информация: Ноутбук HP ENVY x360 14-ES0013DX (7H9Y4UA) / i5-1335U / 8GB / SSD 512GB / 14″, серебристый"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/03/noutbuk-hp-envy-x360-14-es0033dx.png",
        caption=(
            "Ноутбук HP ENVY x360 14-es0033dx (7H9Y1UA) / i7-1355U / 16GB / SSD 1ТB / 14″, серебристый"
            "Артикул: 4404712\n"
            "Цена: 2300 USD\n"
            "Информация: Ноутбук HP ENVY x360 14-es0033dx (7H9Y1UA) / i7-1355U / 16GB / SSD 1ТB / 14″, серебристый"
            ))
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/03/noutbuk-hp-probook-450-g10-1.png",
        caption=(
            "Ноутбук HP ProBook 450 G10 (85B73EA) / i7-1355U / 8GB / SSD 512GB / MX570 2GB / 15.6″, серебристый"
            "Артикул: 244404712\n"
            "Цена: 3000 USD\n"
            "Информация: Ноутбук HP ProBook 450 G10 (85B73EA) / i7-1355U / 8GB / SSD 512GB / MX570 2GB / 15.6″, серебристый"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/03/noutbuk-hp-zbook-firefly-14-g9-1.png",
        caption=(
            "Ноутбук HP ZBook Firefly 14 G9 (417) /Intel Core i7-1270P/ DDR4 16GB/ SSD 512GB/ Intel Iris Xe Graphics/ W11/ RU/ Silver"
            "Артикул: 654404712\n"
            "Цена: 2000 USD\n"
            "Информация: Ноутбук HP ZBook Firefly 14 G9 (417) /Intel Core i7-1270P/ DDR4 16GB/ SSD 512GB/ Intel Iris Xe Graphics/ W11/ RU/ Silver"
            ))
    
@dp.message_handler(text='Телевизоры')
async def show_tvs(message:types.Message):
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/10/58430b44-2615-4894-bfd9-8389186206cc_test.webp",
        caption=(
            "Телевизор Artel 43/9100 TCL"
            "Артикул: 098654404712\n"
            "Цена: 3500 USD\n"
            "Информация: Телевизор Artel 43/9100 TCL"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/10/6512bd43d9caa6e02c990b0a82652dca2023011914063173050drfgschsql-1536x1493.jpg",
        caption=(
            "Телевизор Artel 43AU20H"
            "Артикул: 54404712\n"
            "Цена: 4500 USD\n"
            "Информация: Телевизор Artel 43AU20H"
            ))
    

    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/10/televizor-samsung-ue-32m400-2.png",
        caption=(
            "Телевизор Samsung M4000"
            "Артикул: 432654404712\n"
            "Цена: 5000 USD\n"
            "Информация:Телевизор Samsung UE 32M4000"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2024/07/new-project-9-6-14-10-3-3-4-1.jpg",
        caption=(
            "Телевизор Artel UA43H3502 4K UHD"
            "Артикул: 974404712\n"
            "Цена: 3800 USD\n"
            "Информация: Телевизор Artel UA43H3502 4K UHD"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/10/bez-nazvaniya-1-1.jpg",
        caption=(
            "Телевизор Volto LED 43 Smart"
            "Артикул: 62535612\n"
            "Цена: 4200 USD\n"
            "Информация: Телевизор Volto LED 43 Smart"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/10/televizor-samsung-ue43n5000-2.png",
        caption=(
            "Телевизор Samsung UE43N5000"
            "Артикул: 3642654404712\n"
            "Цена: 5500 USD\n"
            "Информация: Телевизор Samsung UE43N5000"
            ))
    
 
@dp.message_handler(text='Аксесуары со скидкой')
async def show_disas(message:types.Message):
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/01/xiaomi-mi-11.jpg",
    caption=(
            " Телефон:Xiaomi MI 11"
            "Артикул: 654404712\n"
            "Цена: 700 USD\n"
            "Информация: Телефон: Xiaomi MI 11\n"
            "Скидки: 30%"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/01/hp-laser-jet.jpg",
        caption=(
            "Персональный принтер:HP Laser Jet"
            "Артикул: 654404712\n"
            "Цена: 3500 USD\n"
            "Информация:Персональный принтер:HP Laser Jet\n"
            "Скидка 25%"
            ))
    
    await message.answer_photo("https://technoshop.uz/wp-content/uploads/2023/01/white-joy-cons.jpg",
        caption=(
            "Контроллеры: Nintendo"
            "Артикул: 2654404712\n"
            "Цена: 1500 USD\n"
            "Информация: Контроллеры:Обнови свой Nintendo\n"
            "Скидка 10%"
            ))



@dp.message_handler(text='Назад')
async def go_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=start_keyboard)

@dp.message_handler(text="Заказать")
async def order(message:types.Message):
    button = types.KeyboardButton("Запишите ", request_contact=True)
    button = types.KeyboardButton("Отправить контакт", request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста отправьте свой контакт", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message:types.Message):
    await bot.send_message( -4275116284, f'Заявка на заказа:\nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nUsername пользователя: {message.from_user.username}\nТелефон: {message.contact.phone_number}\n')
    await message.answer("Спасибо что заказали\nМы свяжемся с вами в скором времени!")
    await start(message)
   
@dp.message_handler(text='Контакты')
async def contact(message:types.Message):
    await message.reply_contact(first_name='technoshop', phone_number=+998712000660 )
    
executor.start_polling(dp, skip_updates=True)
    
