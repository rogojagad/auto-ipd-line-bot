from singleton.LineClient import LineClient
from linebot.models import (
    TextSendMessage
)

class FollowEventHandler:
    def __init__(self):
        self.lineClient = LineClient()

    def test(self):
        print("Follow event handler loaded")

    def handle(self, event):
        userID = event.source.user_id
        profile = self.lineClient.get_profile(userID)
        firstName = profile.displayName.split(' ')[0]

        self.lineClient.replyMessage(
            event.replyToken,
            TextSendMessage(text="Halo, " + firstName + ", terima kasih sudah follow saya ")
        )


if __name__ == "__main__":
    pass