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
            return self.msgHandler.handle(event)
        if(event.type == 'follow'):
            return self.followHandler.handle(event)

    def test(self, msg):
        return self.msgHandler.handle(msg)
        # pass

if __name__ == "__main__":
    handler = Handler()

    print(handler.test("Test"))