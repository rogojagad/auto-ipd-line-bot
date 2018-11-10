from singleton.LineClient import LineClient

class FollowEventHandler:
    def __init__(self):
        self.lineClient = LineClient()

    def test(self):
        print("Follow event handler loaded")

    def handle(self, event):
        userID = event.source.userId
        profile = self.lineClient.get_profile(userID)
        firstName = profile.displayName.split(' ')[0]
        messages = {
            'type': 'text',
            'text': "Halo, " + firstName + ", terima kasih sudah follow saya "
        }

        self.lineClient.replyMessage(
            event.replyToken,
            messages
        )


if __name__ == "__main__":
    pass