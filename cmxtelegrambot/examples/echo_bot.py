import os

from cmxtelegrambot import create_bot, Message, Storage


PASS = os.environ.get('BOT_PASS')
TOKEN = os.environ.get('BOT_TOKEN')


def on_message(message: Message, _storage: Storage):
    message.reply(f'you sent: {message.text}')

bot = create_bot(TOKEN, password=PASS)
bot.on_message_received(on_message)

bot.start()
