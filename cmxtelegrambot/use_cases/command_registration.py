from cmxtelegrambot.adapters.json_data_storage import JsonChatDataStorage
from cmxtelegrambot.core.services.command import CommandService
from cmxtelegrambot.core.services.authentication import AuthenticationService
from cmxtelegrambot.core.services.bot import BotService
from cmxtelegrambot.dependency_injection import get_storage


def register_command(command_name: str, dispatcher, auth_service: AuthenticationService, callback, secure=False, security_error_message=None):
    storage = get_storage()
    service = CommandService(dispatcher, auth_service, storage)
    service.register(command_name, callback, secure, security_error_message)
