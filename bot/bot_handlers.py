from bot_object import bot
from database import User
from state_handler import get_state_and_process, \
    process_callback_without_state, \
    process_without_state_message
import config


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='choose_language_state'
                        )
            user.save()
        else:
            user.state = 'choose_language_state'
            user.save()
        get_state_and_process(message, user, True)
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
#     try:
        if str(message.chat.id) == config.ADMIN_CHAT_ID:
            process_without_state_message(message)
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='choose_language_state'
                        )
            user.save()
        get_state_and_process(message, user)
    # except Exception as e:
    #     print(e)


@bot.message_handler(content_types=['photo'])
def handle_message(message):
    try:
        if str(message.chat.id) == config.ADMIN_CHAT_ID:
            process_without_state_message(message)
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='choose_language_state'
                        )
            user.save()
        get_state_and_process(message, user)
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user = User.objects(user_id=call.from_user.id).first()
    if user is None:
        user = User(user_id=call.from_user.id,
                    username=call.from_user.username,
                    first_name=call.from_user.first_name,
                    last_name=call.from_user.last_name,
                    state='choose_language_state'
                    )
        user.save()
    process_callback_without_state(call, user)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)
