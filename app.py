import os
import sys
from argparse import ArgumentParser
from handler.webhook.v1.handler import Handler
from flask import Flask, request, abort
from singleton.LineClient import LineClient

from linebot import (
    WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)
eventHandler = Handler()
lineBotApi = LineClient()

channelSecret = os.environ.get("LINE_CHANNEL_SECRET")
handler = WebhookHandler(channelSecret)

@app.route("/test", methods=["GET"])
def test():
    msg = request.args.get("msg")
    return eventHandler.test(msg)

@app.route("/", methods=["GET"])
def about():
     return "Learning Line Bot development using Flask framework"

@app.route("/port", methods=["GET"])
def checkRoute():
    return request.host

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.default()
def handleEvent(event):
    eventHandler.handle(event=event)

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=5000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
