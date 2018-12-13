from singleton.LineClient import LineClient
from linebot.models import (
    TextSendMessage
)
from utils import MessageFactory

import traceback

class MessageEventHandler:
    def __init__(self):
        self.lineClient = LineClient()

    def handle(self, event):
        try:
            self.parseCommand(event)
        except Exception as error:
            print(str(error))

            traceback.print_exc()

    def parseCommand(self, event):
        if (event.message.type != "text"): return

        text = event.message.text.strip().lower()

        if (text.startswith("!isi")):
            pass
        elif (text.startswith("!help")):
            self.simpleReply(event, MessageFactory.helpMessage)
        elif (text.startswith("!about")):
            self.simpleReply(event, MessageFactory.aboutMessage)

    def simpleReply(self, event, msg):
        self.lineClient.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

if __name__ == "__main__":
    pass