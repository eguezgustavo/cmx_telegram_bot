from cmx_telegram_bot import create_bot, Message, Command, Storage

PASS = '********'
TOKEN = '**********************'


def on_hello(command: Command, storage: Storage):
    command.reply('hello from telegram wrapper')
    command.reply(f'saved data {storage.get()}')

bot = create_bot(TOKEN, password=PASS)
bot.add_command('hello', on_hello)

bot.start()
