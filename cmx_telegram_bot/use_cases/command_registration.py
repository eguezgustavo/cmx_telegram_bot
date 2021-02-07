from ..adapters.json_data_storage import JsonChatDataStorage
from ..core.services.command import CommandService
from ..core.services.authentication import AuthenticationService
from ..core.services.bot import BotService
from ..dependency_injection import get_storage


def register_command(command_name: str, dispatcher, auth_service: AuthenticationService, callback, secure=False, security_error_message=None):
    storage = get_storage()
    service = CommandService(dispatcher, auth_service, storage)
    service.register(command_name, callback, secure, security_error_message)
