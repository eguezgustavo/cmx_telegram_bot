from telegram.ext import CommandHandler

from ..data.chat import InternatChatStorage
from ..services.authentication import AuthenticationService
from ..entities.command import Command
from ..entities.storage import Storage


class CommandService:
    def __init__(self, dispatcher, authentication_service: AuthenticationService, chat_storage: InternatChatStorage):
        self.chat_storage = chat_storage
        self.dispatcher = dispatcher
        self.registered_commands = []
        self.authentication_service = authentication_service

    def register(self, command_name, callback, secure=False, security_error_message=None):
        def on_command(update, context):
            chat_id = update.effective_chat.id
            chat_data = self.chat_storage.get(chat_id)
            reply = context.bot.send_message

            command = Command(chat_id, chat_data, reply)

            if not secure or self.authentication_service.is_logged_in(chat_id):
                callback(command, Storage(chat_id, self.chat_storage))
                return
            
            command.reply(security_error_message)

        handler = CommandHandler(command_name, on_command)
        self.dispatcher.add_handler(handler)
        self.registered_commands.append(command_name)
