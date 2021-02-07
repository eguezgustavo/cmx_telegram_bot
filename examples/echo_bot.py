from cmx_telegram_bot import create_bot, Message, Storage


PASS = '28111982'
TOKEN = '1405647753:AAHv42ey2zZ8IqTj4DBgJlzKfqj4tHFRw3o'


def on_message(message: Message, _storage: Storage):
    message.reply(f'you sent: {message.text}')

bot = create_bot(TOKEN, password=PASS)
bot.on_message_received(on_message)

bot.start()
