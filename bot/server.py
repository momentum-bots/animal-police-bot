import flask
from telebot import types
from config import HEROKU_APP_NAME, BOT_TOKEN
from bot_handlers import bot

server = flask.Flask(__name__)

if bot.get_webhook_info().url != 'https://{}.herokuapp.com/{}'.format(HEROKU_APP_NAME, BOT_TOKEN):
    bot.remove_webhook()
    bot.set_webhook(url='https://{}.herokuapp.com/{}'.format(HEROKU_APP_NAME, BOT_TOKEN))


@server.route('/' + BOT_TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode('utf-8'))])
    return 'OK', 200


@server.route('/', methods=['GET'])
def index():
    return 'Home page', 200
