import cmxtelegrambot
import json
import os
from pathlib import Path

from cmxtelegrambot.core.data.chat import InternatChatStorage

DATA_FILE_NAME = 'data.json'
PATH = f'{Path.home()}/telegram_bot'


class JsonChatDataStorage(InternatChatStorage):

    def get_file_name(self, chat_id) -> str:
        file_name = f'{PATH}/{chat_id}_{DATA_FILE_NAME}'

        if not os.path.exists(PATH):
            os.mkdir(PATH)

        if not os.path.exists(file_name):
            with (open(file_name, 'w')) as f:
                json.dump({'id': chat_id}, f)
        
        return file_name

    def get(self, chat_id, key=None):
        chat_data = None
        filename = self.get_file_name(chat_id)
    
        with (open(filename, 'r')) as f:
            chat_data = json.load(f)

        if not key:
            return chat_data
        
        return chat_data.get(key)

    def save(self, chat_id, chat_data=None, **kwargs):
        filename = self.get_file_name(chat_id)
        data = self.get(chat_id)

        with (open(filename, 'w')) as f:
            if chat_data:
                json.dump(chat_data, f)
                return
            
            for key, value in kwargs.items():
                data[key] = value
            json.dump(data, f)        
