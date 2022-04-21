from aiogram.types import ParseMode

# from db import DB, create_txt, Users, create_story_buys
from data import db_session
from data.good import GoodMethods
from utils import TestStates
# from Filters import IsAdmin, IsNumber
from texts import *
from data.users import UserMethods
from keyboards import *

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.markdown import link

from pyqiwip2p import QiwiP2P

API_TOKEN = ''
QIWI_PRIV_KEY = ''

db_session.global_init("db/base.db")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot, dispatcher, data base and pay system
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
# db = DB()
users = UserMethods(db_session)
goods = GoodMethods(db_session)
p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

check_dict = {}


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message):
    chat_id = message.from_user.id
    print(message)
    print(users.get_all_chat_ids())

    if " " in message.text:
        referrer_candidate = message.text.split()[1]
        if referrer_candidate.isdigit():
            referrer_candidate = int(referrer_candidate)
            if referrer_candidate != chat_id and chat_id not in users.get_all_chat_ids():
                referrer = referrer_candidate
                users.add(chat_id, referrer)

            elif chat_id not in users.get_all_chat_ids():
                users.add(chat_id, None)

        elif chat_id not in users.get_all_chat_ids():
            users.add(chat_id, None)

    elif chat_id not in users.get_all_chat_ids():
        users.add(chat_id, None)

    await message.reply("Привет👋\nТут ты можешь купить муравьёв💥 & муравьиные фермы💥", reply_markup=main_kb)
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(None)
    await bot.send_message(598993681, f'новый пользователь: {chat_id}, @{message.from_user.username}')


@dp.message_handler(text='🐜Муравьи', state='*')
async def add_good(message: types.Message):
    all_goods = goods.get_all_goods('ant')
    kb = create_inline_kb(all_goods)
    await message.reply("Выбирайте муравьев", reply_markup=kb)


@dp.message_handler(text='🏠Муравьиные фермы', state='*')
async def add_good(message: types.Message):
    all_goods = goods.get_all_goods('farm')
    kb = create_inline_kb(all_goods)
    await message.reply("Выбирайте муравьиную ферму", reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith('see'), state='*')
async def process_callback_button1(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await bot.delete_message(chat_id, callback_query.message.message_id)
    good_id = int(callback_query.data.split()[-1])
    good = goods.get(good_id)
    await bot.send_photo(chat_id, open(f'images/{good.image_name}', 'rb'),
                         caption=ant_text(good),
                         parse_mode=ParseMode.MARKDOWN,
                         reply_markup=create_ant_inline_kb(good.price, good.id, good.type))


@dp.callback_query_handler(lambda c: c.data.startswith('back'), state='*')
async def process_callback_button1(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    await bot.delete_message(chat_id, callback_query.message.message_id)
    type_ = callback_query.data.split()[-1]
    all_goods = goods.get_all_goods(type_)
    kb = create_inline_kb(all_goods)
    await bot.send_message(chat_id, "Первая инлайн кнопка", reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.startswith('buy'), state='*')
async def process_callback_button1(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    good_id = callback_query.data.split()[1]
    user = users.get(chat_id)
    good = goods.get(good_id)
    if user.balance >= goods.get(good_id).price:
        print('Баланса хватает')
        await bot.send_message(chat_id, f'Поздравляем вы купили {good.name}')
        goods.set_customer(good_id, user.id)
        users.new_purchase(chat_id, good.price)

    else:
        await bot.delete_message(chat_id, callback_query.message.message_id)
        await bot.send_message(chat_id, f'Пополните баланс. Ваш баланс: {users.get(chat_id).balance}₽')


@dp.message_handler(text='🗣Инфо', state='*')
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, info_text)


@dp.message_handler(text='💬Поддержка', state='*')
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, help_text)


@dp.message_handler(text='👤Личный кабинет', state='*')
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    state = dp.current_state(user=chat_id)
    login = message.from_user.username
    user = users.get(chat_id)
    await bot.send_message(chat_id, ls_text(login, user.amount_purchases, user.balance),
                           parse_mode=ParseMode.HTML, reply_markup=ls_kb)


@dp.message_handler(text='🌀Главная')
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '🔮 Главное меню', reply_markup=main_kb)


@dp.message_handler(text='📦История моих покупок', state='*')
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    user = users.get(chat_id)
    if user.purchases:
        for purchase in user.purchases:
            await bot.send_message(chat_id, f'{purchase.name} Стоимость:{purchase.price}')
    else:
        await bot.send_message(chat_id, 'Вы еще ничего не купили')


@dp.message_handler(text='💸Пополнить баланс')
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    state = dp.current_state(user=chat_id)
    await state.set_state(TestStates.all()[1])
    await bot.send_message(chat_id, 'Введите сумму пополнения:')


@dp.message_handler(lambda message: message.text.isdigit(), state=TestStates.PAY_STATE)
async def add_good(message: types.Message):
    chat_id = message.from_user.id
    amount = message.text
    lifetime = 5  # Форма будет жить 5 минут
    comment = 'Пополнение баланса в лучшем мирмикиперском магазине'
    bill = p2p.bill(amount=amount, lifetime=lifetime, comment=comment)
    await bot.send_message(chat_id, pay_text(bill.pay_url, amount), reply_markup=check_kb,
                           parse_mode=ParseMode.MARKDOWN)

    check_dict[chat_id] = bill


@dp.callback_query_handler(lambda c: c.data == 'button_cancel', state=TestStates.PAY_STATE)
async def process_callback_button1(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    if chat_id in check_dict.keys():
        state = dp.current_state(user=chat_id)
        status = p2p.check(bill_id=check_dict[chat_id].bill_id).status
        print(status)
        p2p.reject(bill_id=check_dict[chat_id].bill_id)
        status = p2p.check(bill_id=check_dict[chat_id].bill_id).status
        print(status)
        await state.set_state(None)
        await bot.delete_message(chat_id, callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'button_check', state=TestStates.PAY_STATE)
async def process_callback_button1(callback_query: types.CallbackQuery):
    chat_id = callback_query.from_user.id
    print(check_dict)
    if chat_id in check_dict.keys():
        state = dp.current_state(user=chat_id)
        status = p2p.check(bill_id=check_dict[chat_id].bill_id).status
        print(status)
        if status == 'PAID':
            users.add_balance(chat_id, int(check_dict[chat_id].amount[:-3]))
            await state.set_state(None)
            await bot.edit_message_text('Пополнение произошло успешно!!!',
                                        callback_query.from_user.id,
                                        callback_query.message.message_id)

        if status == 'WAITING':
            await bot.send_message(chat_id, 'Ещё не оплачено')


@dp.message_handler(lambda message: message.from_user.id == 598993681, commands=['admin'])
async def send_welcome(message: types.Message):
    chat_id = 598993681
    state = dp.current_state(user=chat_id)
    await state.set_state(TestStates.all()[0])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
