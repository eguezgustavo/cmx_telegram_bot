from cmx_telegram_bot import create_bot, Message, Command, Storage

PASS = '28111982'
TOKEN = '1405647753:AAHv42ey2zZ8IqTj4DBgJlzKfqj4tHFRw3o'


def on_name_received(message: Message, storage: Storage):
    print('--------', storage)
    message.reply(f'Your name is: {message.text}')

bot = create_bot(TOKEN, password=PASS)
bot.add_input('name', 'Please send me your name', on_name_received)

bot.start()
