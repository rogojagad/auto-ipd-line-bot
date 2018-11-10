from linebot import (
    LineBotApi, WebhookHandler
)
import os

class LineClient:
    def __new__(self):
        if not hasattr(self, 'instance'):
            channelAccessToken = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
            self.instance = LineBotApi(channelAccessToken)

        return self.instance