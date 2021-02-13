from telegram.ext import Updater

from cmxtelegrambot.adapters.json_data_storage import JsonChatDataStorage
from cmxtelegrambot.core.services.bot import BotService
from cmxtelegrambot.core.services.input_command import InputCommandService
from cmxtelegrambot.core.services.authentication import AuthenticationService
from cmxtelegrambot.core.data.chat import InternatChatStorage


def get_storage() -> InternatChatStorage:
    return JsonChatDataStorage()


def get_updater(token):
    return Updater(token=token)


def get_dispatcher(updater):
    return updater.dispatcher


def get_bot_service(dispatcher, storage):
    return BotService(dispatcher, storage)


def get_input_service(dispatcher, storage):
    return InputCommandService(dispatcher, storage)


def get_authentication_service(storage, password):
    return AuthenticationService(storage, password)
