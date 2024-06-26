from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def lang_change():
    kb = [
        [KeyboardButton(text='🇺🇿'),
         KeyboardButton(text='🇷🇺'), ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def shaxs():
    kb = [
        [KeyboardButton(text='yuridikt shaxs'),
         KeyboardButton(text='jismoniy shaxs'), ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def contact_user():
    kb = [
        [KeyboardButton(text='contact', request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    return keyboard
