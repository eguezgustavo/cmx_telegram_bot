import abc


class InternatChatStorage(abc.ABC):

    @abc.abstractmethod
    def get(self, chat_id, key: str = None):
        pass

    @abc.abstractmethod
    def save(self, chat_id, chat_data=None, **kwargs):
        pass
