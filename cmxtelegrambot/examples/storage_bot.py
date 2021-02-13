import os

from cmxtelegrambot import create_bot, Message, Command, Storage

PASS = os.environ.get('BOT_PASS')
TOKEN = os.environ.get('BOT_TOKEN')


def on_message(message: Message, storage: Storage):
    saved_message = storage.get(key='last_message')
    message.reply(f'you sent: {message.text}')
    
    if saved_message:
        message.reply(f'Your last message is {saved_message}')
    else:
        message.reply(f'You do not have any massage saved, saving this one')
    
    storage.save(last_message=message.text)

bot = create_bot(TOKEN, password=PASS)
bot.on_message_received(on_message)

bot.start()
