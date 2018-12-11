from telebot import types
from languages import DICTIONARY


def get_languages_keyboard(language='ww'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['ru_button'])
    keyboard.add(DICTIONARY[language]['ua_button'])
    return keyboard


def get_main_menu_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(DICTIONARY[language]['wanna_take_btn'],
                 DICTIONARY[language]['wanna_leave_btn'])
    keyboard.add(DICTIONARY[language]['lost_btn'])
    keyboard.row(DICTIONARY[language]['wanna_help_btn'],
                 DICTIONARY[language]['info_btn'])
    return keyboard


def get_add_pet_kind_state_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['dog_btn'])
    keyboard.add(DICTIONARY[language]['cat_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_breed_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_name_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['add_pet_no_name_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_sex_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['male_pet_btn'])
    keyboard.add(DICTIONARY[language]['female_pet_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_description_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_lost_pet_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_help_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_age_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_photo_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_add_pet_confirmation_keyboard(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['yes_btn'])
    keyboard.add(DICTIONARY[language]['no_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_want_take_pet_keybord(language='ru'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(DICTIONARY[language]['dog_btn'],
                 DICTIONARY[language]['cat_btn'])
    keyboard.row(DICTIONARY[language]['different_btn'],
                 DICTIONARY[language]['show_all_btn'])
    keyboard.add(DICTIONARY[language]['back_btn'])
    return keyboard


def get_moder_keyboard(language='ru', callback_data='', pet_photo=''):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(
        text=DICTIONARY[language]['url_btn'],
        url=pet_photo)
    keyboard.add(url_btn)
    apply_button = types.InlineKeyboardButton(
        text=DICTIONARY[language]['apply_btn'],
        callback_data=str(callback_data) + 'apply')
    deny_button = types.InlineKeyboardButton(
        text=DICTIONARY[language]['deny_btn'],
        callback_data=str(callback_data) + 'deny')
    keyboard.row(apply_button, deny_button)
    return keyboard


def get_photos_keyboard(language='ru', pets=[]):
    keyboard = types.InlineKeyboardMarkup()
    for idx, pet in enumerate(pets):
        url_btn = types.InlineKeyboardButton(
            text=DICTIONARY[language]['urls_btn'].format(str(idx+1)),
            url=pet.photo_link)
        keyboard.add(url_btn)
    return keyboard


def get_photo_keyboard(language='ru', pet_photo=''):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(
            text=DICTIONARY[language]['url_btn'],
            url=pet_photo)
    keyboard.add(url_btn)
    return keyboard
