from cmxtelegrambot.core.data.chat import InternatChatStorage


class AuthenticationService:
    def __init__(self, storage: InternatChatStorage, password: str):
        self.storage = storage
        self.password = password
    
    def is_logged_in(self, chat_id: str) -> bool:
        return self.storage.get(chat_id, key='authenticated') or False
    
    def log_in(self, chat_id: str, password: str) -> bool:
        if password != self.password:
           return False

        self.storage.save(chat_id, authenticated=True)
        return True
    
    def log_out(self, chat_id: str):
        self.storage.save(chat_id, authenticated=False)
