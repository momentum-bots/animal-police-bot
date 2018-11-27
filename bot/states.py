from bot_object import bot
from languages import DICTIONARY
from keyboards import *


def choose_language_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ww']['choose_language_message'],
                         reply_markup=get_languages_keyboard('ww'))
    else:
        if message.text == DICTIONARY['ww']['ru_button']:
            user.language = 'ru'
            user.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['saved_language_message'])
            return True, 'main_menu_state'
        elif message.text == DICTIONARY['ww']['ua_button']:
            user.language = 'ua'
            user.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['saved_language_message'])
            return True, 'main_menu_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ww']['use_buttons_warning_message'],
                             reply_markup=get_languages_keyboard('ww'))
    return False, ''


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['main_menu_msg'],
                         reply_markup=get_main_menu_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['wanna_take_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['in_progress_msg'])
        elif message.text == DICTIONARY[user.language]['wanna_leave_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['in_progress_msg'])
        elif message.text == DICTIONARY[user.language]['lost_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['in_progress_msg'])
        elif message.text == DICTIONARY[user.language]['wanna_help_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['in_progress_msg'])
        elif message.text == DICTIONARY[user.language]['info_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['in_progress_msg'])
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['use_keyboard_msg'],
                             reply_markup=get_main_menu_keyboard(user.language))
    return False, ''
