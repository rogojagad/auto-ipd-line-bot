import json
from handler.webhook.v1.message.messageHandler import MessageEventHandler
from handler.webhook.v1.follow.followHandler import FollowEventHandler

class Handler:
    def __init__(self):
        self.msgHandler = MessageEventHandler()
        self.followHandler = FollowEventHandler()
        # pass

    def handle(self, event):
        if(event.type == 'message'):
            self.msgHandler.handle(event)
        if(event.type == 'follow'):
            self.followHandler.handle(event)

    def test(self, msg):
        self.msgHandler.handle(msg)
        # pass

if __name__ == "__main__":
    handler = Handler()

    print(handler.test("Test"))