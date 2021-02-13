from cmxtelegrambot.core.data.chat import InternatChatStorage


class Storage:
    def __init__(self, chat_id: str, chat_storage: InternatChatStorage):
        self.__chat_id = chat_id
        self.__chat_storage = chat_storage
    
    def get(self, key=None):
        return self.__chat_storage.get(self.__chat_id, key=key)
    
    def save(self, **kwargs):
        return self.__chat_storage.save(self.__chat_id, **kwargs)
