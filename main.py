from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text

token = ''

bot = Bot(token=token)
dp = Dispatcher(bot)

basket = []
pay = 0

@dp.message_handler(commands="start")
async def start(message: types.Message):
    global pay
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Меню", "Акции", "Техническая поддержка", 'Оформить заказ']
    keyboard.add(*buttons)
    pay = 0
    basket.clear()
    await message.answer("Здравствуйте\nДобро пожаловать в онлайн пиццерию\nЧто вы хотите посмотреть?", reply_markup=keyboard)
    await bot.send_photo(chat_id=message.chat.id, photo=open('PIZZA.jpg', 'rb'))


@dp.message_handler(Text(equals="Меню"))
async def menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Пицца', 'Напитки', 'Десерты', 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Что вы хотите посмотреть?", reply_markup=keyboard)



@dp.message_handler(Text(equals="Пицца"))
async def pizza(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Пепперони', '4 сыра', 'Маргарита', 'Сырная с ветчиной', 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Список наших пицц:\nПепперони - 699 рублей\n4 сыра - 499 рублей\nМаргарита - 499 рублей\nСырная с ветчиной - 599 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Пепперони"))
async def pizza1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Купить: Пепперони', 'Вернуться обратно']
    keyboard.add(*buttons)
    await bot.send_photo(chat_id=message.chat.id, photo=open('pepperoni.png', 'rb'))
    await message.answer("Пепперони\n\nЦена: 699 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="4 сыра"))
async def pizza2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Купить: 4 сыра', 'Вернуться обратно']
    keyboard.add(*buttons)
    await bot.send_photo(chat_id=message.chat.id, photo=open('4 cheese.png', 'rb'))
    await message.answer("4 сыра\n\nЦена: 499 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Маргарита"))
async def pizza3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Купить: Маргарита', 'Вернуться обратно']
    keyboard.add(*buttons)
    await bot.send_photo(chat_id=message.chat.id, photo=open('margarita.png', 'rb'))
    await message.answer("Маргарита\n\nЦена: 499 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Сырная с ветчиной"))
async def pizza4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Купить: Сырная с ветчиной', 'Вернуться обратно']
    keyboard.add(*buttons)
    await bot.send_photo(chat_id=message.chat.id, photo=open('cheese with pork.png', 'rb'))
    await message.answer("Сырная с ветчиной\n\nЦена: 599 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить: Пепперони"))
async def buy_pizza1(message: types.Message):
    global pay
    pay += 699
    basket.append('Пепперони')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить: Маргарита"))
async def buy_pizza2(message: types.Message):
    global pay
    pay += 499
    basket.append('Маргарита')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить: 4 сыра"))
async def buy_pizza3(message: types.Message):
    global pay
    pay += 499
    basket.append('4 сыра')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить: Сырная с ветчиной"))
async def buy_pizza4(message: types.Message):
    global pay
    pay += 599
    basket.append('Сырная с ветчиной')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)



@dp.message_handler(Text(equals="Акции"))
async def stocks(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1+1=3", '2 по цене 1', 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Вот, все акции на нашу продукцию:", reply_markup=keyboard)

@dp.message_handler(Text(equals="1+1=3"))
async def stock3_for_2_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Воспользоваться: 1+1=3", 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Акция 3 пиццы по цене 2", reply_markup=keyboard)
    await message.answer('В данной акции пицца Маргарита идет в подарок к двум пиццам Пепперони')
    await bot.send_photo(chat_id=message.chat.id, photo=open('1+1=3.jpg', 'rb'))

@dp.message_handler(Text(equals="2 по цене 1"))
async def stock2_for_1_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Воспользоваться: 2 по цене 1", 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Акция: пицца в подарок", reply_markup=keyboard)
    await message.answer("В данной акции пицца 4 сыра идет в подарок к пицце Сырная с ветчиной")
    await bot.send_photo(chat_id=message.chat.id, photo=open('2_for_1_new.png', 'rb'))

@dp.message_handler(Text(equals="Воспользоваться: 1+1=3"))
async def buy_stock3_for_2_price(message: types.Message):
    global pay
    pay += 699 * 2
    basket.append('Пепперони')
    basket.append('Пепперони')
    basket.append('Маргарита')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Воспользоваться: 2 по цене 1"))
async def buy_stock2_for_1_price(message: types.Message):
    global pay
    pay += 599
    basket.append('Сырная с ветчиной')
    basket.append('4 сыра')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)



@dp.message_handler(Text(equals="Напитки"))
async def drinks(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Купить Латте", 'Купить Капучино', 'Купить Черный чай', 'Купить Зеленый чай', 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Все напитки доступные в нашем меню:\n\nЛатте(0.4) - 119 рублей\nКапучино(0.4) - 99 рублей\nЧерный чай(0.4) - 79 рублей\nЗеленый чай(0.4) - 79 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить Латте"))
async def drinks1(message: types.Message):
    global pay
    pay += 119
    basket.append('Латте')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить Капучино"))
async def drinks2(message: types.Message):
    global pay
    pay += 99
    basket.append('Капучино')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить Черный чай"))
async def drinks3(message: types.Message):
    global pay
    pay += 79
    basket.append('Черный чай')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить Зеленый чай"))
async def drinks4(message: types.Message):
    global pay
    pay += 79
    basket.append('Зеленый чай')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)



@dp.message_handler(Text(equals="Десерты"))
async def desserts(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Тирамису', 'Панна котта', 'Вернуться обратно']
    keyboard.add(*buttons)
    await message.answer("Список наших десертов:", reply_markup=keyboard)

@dp.message_handler(Text(equals="Тирамису"))
async def dessert1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Купить: Тирамису', 'Вернуться обратно']
    keyboard.add(*buttons)
    await bot.send_photo(chat_id=message.chat.id, photo=open('desert-pirozhnoe-tiramisu-krem-myata.jpg', 'rb'))
    await message.answer("Тирамису\n\nЦена: 399 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Панна котта"))
async def dessert2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Купить: Панна котта', 'Вернуться обратно']
    keyboard.add(*buttons)
    await bot.send_photo(chat_id=message.chat.id, photo=open('Panna-kota.jpg', 'rb'))
    await message.answer("Панна котта\n\nЦена: 399 рублей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить: Тирамису"))
async def buy_dessert1(message: types.Message):
    global pay
    pay += 399
    basket.append('Тирамису')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)

@dp.message_handler(Text(equals="Купить: Панна котта"))
async def buy_dessert2(message: types.Message):
    global pay
    pay += 399
    basket.append('Панна котта')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Вернуться обратно', 'Оформить заказ']
    keyboard.add(*buttons)
    basket_new = ', '.join(basket)
    await message.reply(f'Ваша корзина: {basket_new}, сумма к оплате {pay} рублей', reply_markup=keyboard)



@dp.message_handler(Text(equals="Вернуться обратно"))
async def back(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Меню", "Акции", "Техническая поддержка", 'Оформить заказ']
    keyboard.add(*buttons)
    await message.answer("Что вы хотите посмотреть?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Техническая поддержка"))
async def helper(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = ['Вернуться обратно']
    keyboard.add(*button)
    await message.answer("Связаться с технической поддержкой вы можете по телефону: \n+7(999)999-99-99", reply_markup=keyboard)

@dp.message_handler(Text(equals='Оформить заказ'))
async def zakaz(message: types.Message):
    await message.reply('Введите адрес для доставки')
    @dp.message_handler()
    async def echo_message1(message: types.Message):
        adrees = message.text
        if pay == 0:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('Вернуться обратно')
            await message.answer('Вы ничего не заказали')
        else:
            basket_new = '; '.join(basket)
            await message.answer(f"Ваш заказ: {basket_new}\nК оплате: {pay} рублей\nЧерез 40 минут заказ будет доставлен по адресу: {adrees}")



if __name__ == '__main__':
    executor.start_polling(dp)
