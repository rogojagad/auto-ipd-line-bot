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
        firstName = profile.display_name.split(' ')[0]

        self.lineClient.reply_message(
            event.reply_token,
            TextSendMessage(text="Halo, " + firstName + ", terima kasih sudah follow saya ")
        )


if __name__ == "__main__":
    pass