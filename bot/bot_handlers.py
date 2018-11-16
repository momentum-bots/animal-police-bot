from bot_object import bot
from database import User


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='start'
                        )
            user.save()
            bot.send_message(message.chat.id,
                             'Даров, {}!'.format(user.first_name))
        else:
            bot.send_message(message.chat.id,
                             'Даров, {}! Ты нам уже писал.'.format(user.first_name))
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        bot.send_message(message.chat.id,
                         'Yes, human! We are animals!')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.polling(none_stop=True)
