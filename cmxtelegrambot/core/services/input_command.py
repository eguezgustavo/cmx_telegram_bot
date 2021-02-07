import enum

from telegram.ext import CommandHandler

from ..data.chat import InternatChatStorage
from ..entities.command import Command
from ..entities.message import Message


class InputCommandService:

    WAITING = 1
    IDLE = 2

    def __init__(self, dispatcher, chat_storage: InternatChatStorage):
        self.chat_storage = chat_storage
        self.dispatcher = dispatcher

    def register(self, command_name, input_title):
        def on_command(update, context):
            chat_id = update.effective_chat.id
            input_state = self.chat_storage.get(chat_id, key='input_state') or {command_name: {'state': InputCommandService.WAITING}}

            updated_input_state = {
                input_name: { 'state': InputCommandService.IDLE }
                for input_name in input_state.keys() if input_name != command_name
            }
            updated_input_state[command_name] = { 'state': InputCommandService.WAITING }

            self.chat_storage.save(chat_id, input_state=updated_input_state)
            context.bot.send_message(chat_id=chat_id, text=input_title)

        command_handler = CommandHandler(command_name, on_command)
        self.dispatcher.add_handler(command_handler)
