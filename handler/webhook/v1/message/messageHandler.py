from singleton.LineClient import LineClient
from linebot.models import (
    TextSendMessage
)

class MessageEventHandler:
    def __init__(self):
        self.lineClient = LineClient()

    def handle(self, event):
        # return event.message.text
        userId = event.source.userId

        profile = self.lineClient.get_profile(userId)

        print(profile.displayName)

        self.lineClient.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

    def test(self):
        print("Message event handler loaded")

if __name__ == "__main__":
    pass