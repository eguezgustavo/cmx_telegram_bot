from cmx_telegram_bot import create_bot, Message, Command, Storage

PASS = '********'
TOKEN = '**********************'


def on_test(command: Command, storage: Storage):
    command.reply('Test command received')


bot = create_bot(TOKEN, password=PASS)
bot.add_command('test', on_test, secured=True, security_error_message='The name command requieres authentication')
bot.use_authentication(
    'login',
    'Please send your password',
    'Already authenticated',
    'Authentication error',
    'Login OK'
)

bot.start()
