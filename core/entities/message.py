class Message:
    def __init__(self, chat_id, chat_data, reply, text):
        self.chat_id = chat_id
        self.chat_data = chat_data
        self.bot_reply = reply
        self.text = text

    def reply(self, text):
        self.bot_reply(chat_id=self.chat_id, text=text)
