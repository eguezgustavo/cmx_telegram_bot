import os

from cmxtelegrambot import create_bot, Message, Command, Storage

PASS = os.environ.get('BOT_PASS')
TOKEN = os.environ.get('BOT_TOKEN')


def on_name_received(message: Message, storage: Storage):
    print('--------', storage)
    message.reply(f'Your name is: {message.text}')

bot = create_bot(TOKEN, password=PASS)
bot.add_input('name', 'Please send me your name', on_name_received)

bot.start()
