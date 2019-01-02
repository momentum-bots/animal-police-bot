def send_message_to_users(bot, users, message_text):
    for user in users:
        try:
            bot.send_message(user.user_id, message_text)
        except Exception as e:
            print(e)
