import logging

from telegram.ext import MessageHandler, Filters

from cmxtelegrambot.core.data.chat import InternatChatStorage
from cmxtelegrambot.core.entities.message import Message
from cmxtelegrambot.core.entities.storage import Storage


class BotService:

    def __init__(self, updater, chat_storage: InternatChatStorage):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.chat_storage = chat_storage
        self.updater = updater
        self.message_callbacks = []

    def __on_message(self, update, context):
        chat_id = update.effective_chat.id
        chat_data = self.chat_storage.get(chat_id)
        text = update.message.text
        reply = context.bot.send_message
        message = Message(chat_id, chat_data, reply, text)
        for callback in self.message_callbacks:
            storage = Storage(chat_id, self.chat_storage)
            callback(message, storage)

    def on_message(self, function):
        self.message_callbacks.append(function)

    def start(self):
        self.updater.start_polling()
        input_handler = MessageHandler(Filters.text & (~Filters.command), self.__on_message)
        self.updater.dispatcher.add_handler(input_handler)
