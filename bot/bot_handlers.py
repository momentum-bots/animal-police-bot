from bot_object import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id,
                         'Hello, human! We are animals!')
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
