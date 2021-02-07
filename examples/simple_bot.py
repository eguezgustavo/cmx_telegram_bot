from cmx_telegram_bot import create_bot, Message, Command, Storage

PASS = '28111982'
TOKEN = '1405647753:AAHv42ey2zZ8IqTj4DBgJlzKfqj4tHFRw3o'


def on_hello(command: Command, storage: Storage):
    command.reply('hello from telegram wrapper')
    command.reply(f'saved data {storage.get()}')

bot = create_bot(TOKEN, password=PASS)
bot.add_command('hello', on_hello)

bot.start()
