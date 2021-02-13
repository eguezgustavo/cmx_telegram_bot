from cmxtelegrambot.core.services.input_command import InputCommandService
from cmxtelegrambot.core.services.bot import BotService
from cmxtelegrambot.adapters.json_data_storage import JsonChatDataStorage
from cmxtelegrambot.core.data.chat import InternatChatStorage
from cmxtelegrambot.core.entities.message import Message
from cmxtelegrambot.core.services.authentication import AuthenticationService
from cmxtelegrambot.dependency_injection import get_storage


def use_authentication(
    login_command_name: str,
    login_text: str,
    already_authenticated_message: str,
    authentication_error_message: str,
    login_successful_message: str,
    password: str,
    authentication_service: AuthenticationService,
    bot: BotService,
    input_service: InputCommandService,
    register_input,
    storage: InternatChatStorage
):
    def on_pass_received(message: Message):
        if authentication_service.is_logged_in(message.chat_id):
            message.reply(already_authenticated_message)
        else:
            if authentication_service.log_in(message.chat_id,  message.text):
                message.reply(login_successful_message)
            else:
                message.reply(authentication_error_message)

    register_input(login_command_name, login_text, bot, input_service, on_pass_received, storage)
