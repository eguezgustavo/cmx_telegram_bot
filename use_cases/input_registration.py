from ..adapters.json_data_storage import JsonChatDataStorage
from ..core.services.input_command import InputCommandService
from ..core.services.bot import BotService
from ..core.entities.message import Message
from ..core.entities.storage import Storage
from ..core.data.chat import InternatChatStorage


def register_input(command_name: str, input_title: str, bot: BotService, input_service: InputCommandService, callback, chat_storage: InternatChatStorage):
    
    @bot.on_message
    def response_receiver(message: Message, chat_data):
        input_state = chat_data.get('input_state')
        for input_command, input_information in input_state.items():
            if input_command == command_name and input_information['state'] == InputCommandService.WAITING:
                callback(message, Storage(message.chat_id, chat_storage))

    input_service.register(command_name, input_title)
