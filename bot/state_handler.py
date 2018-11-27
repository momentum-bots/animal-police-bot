from database import User
from states import *

states = {'choose_language_state': choose_language_state,
          'main_menu_state': main_menu_state}


def get_state_and_process(message, user: User, is_entry=False):
    if user.state in states:
        change_state, state_to_change_name = states[user.state](message, user, is_entry)
    else:
        user.state = 'choose_language_state'
        user.save()
        change_state, state_to_change_name = states[user.state](message, user, is_entry)
    if change_state:
        go_to_state(message, state_to_change_name, user)


def go_to_state(message, state_name: str, user: User):
    user.state = state_name
    user.save()
    get_state_and_process(message, user, is_entry=True)
