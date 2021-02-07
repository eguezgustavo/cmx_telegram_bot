from cmx_telegram_bot import create_bot, Message, Command, Storage


PASS = '28111982'
TOKEN = '1405647753:AAHv42ey2zZ8IqTj4DBgJlzKfqj4tHFRw3o'


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
