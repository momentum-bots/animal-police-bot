from bot_object import bot
from keyboards import *
from config import ADMIN_CHAT_ID

from database import Pet, User
from mongoengine import Q

import re


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
            return True, 'want_take_pet_state'

        elif message.text == DICTIONARY[user.language]['wanna_leave_btn']:
            return True, 'add_pet_kind_state'
        elif message.text == DICTIONARY[user.language]['lost_btn']:
            return True, 'lost_pet_state'

        elif message.text == DICTIONARY[user.language]['wanna_help_btn']:
            return True, 'help_state'

        elif message.text == DICTIONARY[user.language]['info_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['in_progress_msg'])
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['use_keyboard_msg'],
                             reply_markup=get_main_menu_keyboard(user.language))
    return False, ''


def lost_pet_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['lost_msg'],
                         reply_markup=get_lost_pet_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['back_btn']:
            return True, 'main_menu_state'
        else:
            bot.send_message(ADMIN_CHAT_ID,
                             '{0}\n<a href="tg://user?id={1}">{2}</a>'.format(
                                 message.text,
                                 user.user_id,
                                 DICTIONARY[user.language]['owner_user']),
                             parse_mode='HTML')
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_lost_msg'])
            return True, 'main_menu_state'

    return False, ''


def help_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['help_money_msg'],
                         reply_markup=get_help_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['back_btn']:
            return True, 'main_menu_state'
        else:
            return True, 'main_menu_state'

    return False, ''


def add_pet_kind_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['add_pet_kind_msg'],
                         reply_markup=get_add_pet_kind_state_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['dog_btn']:
            pet = Pet(user_id=user.user_id,
                      kind=DICTIONARY[user.language]['dog'])
            pet.save()
            user.current_pet = pet.pet_id
            user.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_breed_state'
        elif message.text == DICTIONARY[user.language]['cat_btn']:
            pet = Pet(user_id=user.user_id,
                      kind=DICTIONARY[user.language]['cat'])
            pet.save()
            user.current_pet = pet.pet_id
            user.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_breed_state'
        elif message.text == DICTIONARY[user.language]['back_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            return True, 'main_menu_state'
        else:
            pet = Pet(user_id=user.user_id,
                      kind=message.text)
            pet.save()
            user.current_pet = pet.pet_id
            user.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_breed_state'

    return False, ''


def add_pet_breed_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['add_pet_breed_msg'],
                         reply_markup=get_add_pet_breed_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['back_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            return True, 'main_menu_state'
        else:
            pet = Pet.objects(pet_id=user.current_pet).first()
            pet.breed = message.text
            pet.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_sex_state'

    return False, ''


def add_pet_sex_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['add_pet_sex_msg'],
                         reply_markup=get_add_pet_sex_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['male_pet_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            pet.sex = False
            pet.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_description_state'
        elif message.text == DICTIONARY[user.language]['female_pet_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            pet.sex = True
            pet.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_description_state'
        elif message.text == DICTIONARY[user.language]['back_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            return True, 'main_menu_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['use_keyboard_msg'],
                             reply_markup=get_add_pet_sex_keyboard(user.language))

    return False, ''


def add_pet_description_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['add_pet_description_msg'],
                         reply_markup=get_add_pet_description_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['back_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            return True, 'main_menu_state'
        else:
            pet = Pet.objects(pet_id=user.current_pet).first()
            pet.description = message.text
            pet.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_age_state'

    return False, ''


def add_pet_age_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['add_pet_age_msg'],
                         reply_markup=get_add_pet_age_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['back_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            return True, 'main_menu_state'
        else:
            pet = Pet.objects(pet_id=user.current_pet).first()
            pet.age = message.text
            pet.save()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['ok_msg'])
            return True, 'add_pet_confirmation_state'

    return False, ''


def add_pet_confirmation_state(message, user, is_entry=False):
    if is_entry:
        pet = Pet.objects(pet_id=user.current_pet).first()
        message_answer = DICTIONARY[user.language]['add_pet_confirmation_state']
        message_answer += DICTIONARY[user.language]['print_info_msg'].format(pet.kind,
                                                                             (DICTIONARY[user.language][
                                                                                  'female_pet_btn']
                                                                              if pet.sex else
                                                                              DICTIONARY[user.language][
                                                                                  'male_pet_btn']),
                                                                             pet.breed, pet.age,
                                                                             pet.description, pet.user_id)
        bot.send_message(message.chat.id,
                         message_answer,
                         parse_mode='HTML',
                         reply_markup=get_add_pet_confirmation_keyboard(user.language))
    else:
        if message.text == DICTIONARY[user.language]['yes_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            # pet.view = True
            pet.save()
            bot.send_message(ADMIN_CHAT_ID,
                             DICTIONARY[user.language]['print_info_msg'].format(
                                 pet.kind,
                                 (DICTIONARY[user.language]['female_pet_btn'] if pet.sex else
                                  DICTIONARY[user.language]['male_pet_btn']),
                                 pet.breed,
                                 pet.age,
                                 pet.description,
                                 pet.user_id),
                             reply_markup=get_moder_keyboard(language=user.language,
                                                             callback_data=pet.pet_id),
                             parse_mode='html')
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['add_ok_pet_msg'])
            return True, 'main_menu_state'
        elif message.text == DICTIONARY[user.language]['no_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['add_no_pet_msg'])
            return True, 'main_menu_state'
        elif message.text == DICTIONARY[user.language]['back_btn']:
            pet = Pet.objects(pet_id=user.current_pet).first()
            if pet:
                pet.delete()
            return True, 'main_menu_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['use_keyboard_msg'],
                             reply_markup=get_add_pet_confirmation_keyboard(user.language))

    return False, ''


def want_take_pet_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY[user.language]['want_take_pet_msg'],
                         reply_markup=get_want_take_pet_keybord(user.language))
    else:
        if message.text == DICTIONARY[user.language]['dog_btn']:
            message_answer = ''
            for pet in Pet.objects(Q(kind=DICTIONARY['ua']['dog']) | Q(kind=DICTIONARY['ru']['dog'])):
                if pet.view:
                    message_answer += DICTIONARY[user.language]['print_info_msg'].format(pet.kind,
                                                                                         (DICTIONARY[user.language][
                                                                                              'female_pet_btn']
                                                                                          if pet.sex else
                                                                                          DICTIONARY[user.language][
                                                                                              'male_pet_btn']),
                                                                                         pet.breed, pet.age,
                                                                                         pet.description, pet.user_id)
            if message_answer == '':
                bot.send_message(message.chat.id,
                                 DICTIONARY[user.language]['not_found_pet_msg'],
                                 parse_mode='HTML')
            else:
                bot.send_message(message.chat.id,
                                 message_answer,
                                 parse_mode='HTML')
        elif message.text == DICTIONARY[user.language]['cat_btn']:
            message_answer = ''
            for pet in Pet.objects(Q(kind=DICTIONARY['ua']['cat']) | Q(kind=DICTIONARY['ru']['cat'])):
                if pet.view:
                    message_answer += DICTIONARY[user.language]['print_info_msg'].format(pet.kind,
                                                                                         (DICTIONARY[user.language][
                                                                                              'female_pet_btn']
                                                                                          if pet.sex else
                                                                                          DICTIONARY[user.language][
                                                                                              'male_pet_btn']),
                                                                                         pet.breed, pet.age,
                                                                                         pet.description, pet.user_id)
            if message_answer == '':
                bot.send_message(message.chat.id,
                                 DICTIONARY[user.language]['not_found_pet_msg'],
                                 parse_mode='HTML')
            else:
                bot.send_message(message.chat.id,
                                 message_answer,
                                 parse_mode='HTML')
        elif message.text == DICTIONARY[user.language]['different_btn']:
            message_answer = ''
            for pet in Pet.objects():
                if pet.view and pet.kind != DICTIONARY['ru']['dog'] and pet.kind != DICTIONARY['ru']['cat']  \
                        and pet.kind != DICTIONARY['ua']['dog'] and pet.kind != DICTIONARY['ua']['cat']:
                    message_answer += DICTIONARY[user.language]['print_info_msg'].format(pet.kind,
                                                                                         (DICTIONARY[user.language][
                                                                                              'female_pet_btn']
                                                                                          if pet.sex else
                                                                                          DICTIONARY[user.language][
                                                                                              'male_pet_btn']),
                                                                                         pet.breed, pet.age,
                                                                                         pet.description, pet.user_id)
            if message_answer == '':
                bot.send_message(message.chat.id,
                                 DICTIONARY[user.language]['not_found_pet_msg'],
                                 parse_mode='HTML')
            else:
                bot.send_message(message.chat.id,
                                 message_answer,
                                 parse_mode='HTML')
        elif message.text == DICTIONARY[user.language]['show_all_btn']:
            message_answer = ''
            for pet in Pet.objects():
                if pet.view:
                    message_answer += DICTIONARY[user.language]['print_info_msg'].format(pet.kind,
                                                                                         (DICTIONARY[user.language][
                                                                                              'female_pet_btn']
                                                                                          if pet.sex else
                                                                                          DICTIONARY[user.language][
                                                                                              'male_pet_btn']),
                                                                                         pet.breed, pet.age,
                                                                                         pet.description, pet.user_id)
            if message_answer == '':
                bot.send_message(message.chat.id,
                                 DICTIONARY[user.language]['not_found_pet_msg'],
                                 parse_mode='HTML')
            else:
                bot.send_message(message.chat.id,
                                 message_answer,
                                 parse_mode='HTML')
        elif message.text == DICTIONARY[user.language]['back_btn']:
            return True, 'main_menu_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY[user.language]['use_keyboard_msg'],
                             reply_markup=get_want_take_pet_keybord(user.language))
    return False, ''


def callback_handler(call, user):
    pet = Pet.objects(pet_id=re.search('[0-9]+', call.data).group()).first()
    if pet:
        if 'apply' in call.data:
            pet.view = True
            pet.save()
            user = User.objects(user_id=pet.user_id).first()
            if user:
                bot.send_message(
                    user.user_id,
                    DICTIONARY[user.language]['applied_msg']
                )
        else:
            user = User.objects(user_id=pet.user_id).first()
            if user:
                bot.send_message(
                    user.user_id,
                    DICTIONARY[user.language]['denied_msg']
                )
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=types.InlineKeyboardMarkup()
        )
    else:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='X'
        )
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=types.ReplyKeyboardRemove())
    bot.answer_callback_query(call.id)


def admin_chat_event_handler(message):
    animal_id = re.search('[0-9]+', message.text).group()
    print(animal_id)


def inline_callback_handler(call, user):
    bot.answer_callback_query(call.id)
