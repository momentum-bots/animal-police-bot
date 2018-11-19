from database import User
from states import *

states = {'choose_language_state': choose_language_state}


def get_state_and_process(message, user: User, is_entry=False):
    if user.state in states:
        states[user.state](message, user, is_entry)
    else:
        user.state = 'choose_language_state'
        user.save()
        states[user.state](message, user, is_entry)


def go_to_state(state_name: str, user: User):
    user.state = state_name
    user.save()
    get_state_and_process(state_name, user, is_entry=True)
