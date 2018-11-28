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


def get_add_pet_kind_state_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['dog_btn'])
    keyboard.add(DICTIONARY[language]['cat_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_breed_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_sex_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['male_pet_btn'])
    keyboard.add(DICTIONARY[language]['female_pet_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_description_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_lost_pet_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_help_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_age_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_confirmation_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['yes_btn'])
    keyboard.add(DICTIONARY[language]['no_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_want_take_pet_keybord(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(DICTIONARY[language]['dog_btn'],
                 DICTIONARY[language]['cat_btn'])
    keyboard.row(DICTIONARY[language]['different_btn'],
                 DICTIONARY[language]['show_all_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard
