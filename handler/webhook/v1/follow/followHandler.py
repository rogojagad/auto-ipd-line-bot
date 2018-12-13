from handler
from singleton.LineClient import LineClient
from linebot.models import (
    TextSendMessage
)
from utils import MessageFactory

class FollowEventHandler:
    def __init__(self):
        self.lineClient = LineClient()

    def test(self):
        print("Follow event handler loaded")

    def handle(self, event):
        userID = event.source.user_id
        profile = self.lineClient.get_profile(userID)
        firstName = profile.display_name.split(' ')[0]

        self.lineClient.reply_message(
            event.reply_token,
            TextSendMessage(text = MessageFactory.followMessage(firstName)
            )
        )
        
if __name__ == "__main__":
    pass