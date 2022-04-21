from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('🐜Муравьи'),
                                                        KeyboardButton('🏠Муравьиные фермы'),
                                                        KeyboardButton('👤Личный кабинет'),
                                                        KeyboardButton('🗣Инфо'),
                                                        KeyboardButton('💬Поддержка'))


def create_inline_kb(goods):
    kb = InlineKeyboardMarkup()
    for good in goods:
        kb.add(InlineKeyboardButton(f'{good.name}', callback_data=f'see {good.id}'))
    return kb


def create_ant_inline_kb(price, id, type):
    kb = InlineKeyboardMarkup()
    kb.row(InlineKeyboardButton('Назад', callback_data=f'back {type}'),
           InlineKeyboardButton(f'Купить {price}', callback_data=f'buy {id}'))
    return kb


ls_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('🌀Главная')) \
    .row(KeyboardButton('📦История моих покупок'), KeyboardButton('💸Пополнить баланс'))


check_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True). \
    add(InlineKeyboardButton(f'Проверить', callback_data='button_check'),
        InlineKeyboardButton(f'Отмена', callback_data='button_cancel'))