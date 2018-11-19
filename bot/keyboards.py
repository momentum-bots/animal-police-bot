from telebot import types
from languages import DICTIONARY


def get_languages_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['ru_button'])
    keyboard.add(DICTIONARY[language]['ua_button'])
    return keyboard
