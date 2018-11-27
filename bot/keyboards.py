from telebot import types
from languages import DICTIONARY


def get_languages_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['ru_button'])
    keyboard.add(DICTIONARY[language]['ua_button'])
    return keyboard


def get_main_menu_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(DICTIONARY[language]['wanna_take_btn'],
                 DICTIONARY[language]['wanna_leave_btn'])
    keyboard.add(DICTIONARY[language]['lost_btn'])
    keyboard.row(DICTIONARY[language]['wanna_help_btn'],
                 DICTIONARY[language]['info_btn'])
    return keyboard
