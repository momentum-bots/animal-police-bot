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
        elif message.text == DICTIONARY['ww']['ua_button']:
            user.language = 'ua'
            user.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['saved_language_message'])
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ww']['use_buttons_warning_message'],
                             reply_markup=get_languages_keyboard('ww'))
