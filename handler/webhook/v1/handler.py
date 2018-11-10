import json
import loader

import messageHandler
import followHandler

class Handler:
    def __init__(self):
        self.msgHandler = messageHandler.MessageEventHandler()
        self.followHandler = followHandler.FollowEventHandler()
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