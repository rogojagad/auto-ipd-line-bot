from singleton.LineClient import LineClient
from linebot.models import (
    TextSendMessage
)

class MessageEventHandler:
    def __init__(self):
        self.lineClient = LineClient()

    def handle(self, event):
        # return event.message.text

        messages = {
            'type' : 'text',
            'text' : event.message.text
        }

        self.lineClient.reply_message(
            event.reply_token,
            messages
        )

    def test(self):
        print("Message event handler loaded")

if __name__ == "__main__":
    pass