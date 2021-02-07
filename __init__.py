import typing

from .core.services.bot import BotService
from .core.services.input_command import InputCommandService

from .dependency_injection import get_storage, get_dispatcher, get_bot_service, get_input_service, get_updater, get_authentication_service
from .use_cases.command_registration import register_command
from .use_cases.input_registration import register_input
from .use_cases.use_authentication import use_authentication
from .use_cases.use_start import use_start, CommandDescription

from .core.entities.message import Message
from .core.entities.command import Command
from .core.entities.storage import Storage


class Bot:
    def __init__(self, token, password=None, storage=None, dispatcher=None, bot_service=None, input_service=None, authentication_service=None):
        self.storage = storage
        self.dispatcher = dispatcher
        self.bot_service = bot_service
        self.input_service = input_service
        self.authentication_service = authentication_service
        self.on_message_received: typing.Callable[[Message, any], None] = self.bot_service.on_message
        self.start_title = None
        self.commands_list = []
        self.password = password
    
    def add_command(self, command_name, callback, secured=False, security_error_message=None):
        register_command(command_name, self.dispatcher, self.authentication_service, callback, secured, security_error_message)

    def add_input(self, command_name: str, input_title: str, callback: typing.Callable[[Message], None]):
        register_input(command_name, input_title, self.bot_service, self.input_service, callback, self.storage)
    
    def use_authentication(
        self,
        command_name,
        login_text,
        already_authenticated_message,
        authentication_error_message,
        login_successful_message
    ):
        use_authentication(
            command_name,
            login_text,
            already_authenticated_message,
            authentication_error_message,
            login_successful_message,
            self.password,
            self.authentication_service,
            self.bot_service,
            self.input_service,
            register_input,
            self.storage
        )
    
    def use_start(self, start_command_title: str):
        self.start_title = start_command_title
        return self

    def add_command_to_start(self, name: str, description: str):
        self.commands_list.append(CommandDescription(name, description))
        return self

    def start(self):
        self.bot_service.start()
        if self.commands_list:
            use_start(self.start_title, self.commands_list, register_command, self.dispatcher, self.authentication_service)


def create_bot(token, password=None):
    storage = get_storage()
    updater = get_updater(token)
    dispatcher = get_dispatcher(updater)
    bot_service = get_bot_service(updater, storage)
    input_service = get_input_service(dispatcher, storage)
    authentication_service = get_authentication_service(storage, password)

    return Bot(token, **{
        'storage': storage,
        'dispatcher': dispatcher,
        'bot_service': bot_service,
        'input_service': input_service,
        'authentication_service': authentication_service,
        'password': password,
    })
