from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

import random

app = Flask(__name__)

# ▼ env file loading
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

line_bot_api = LineBotApi(os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]);
handler = WebhookHandler(os.environ["YOUR_CHANNEL_SECRET"]);

# ▼ Connecting to the LINE Messaging API
# 【指定】${ ngrok url }/callback  ⇒ (LINE Dev)　Webhook
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # parse webhook body
    try:
        print('■body : ', body)
        print('■signature : ', signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# ▼ text manipulation
@handler.add(MessageEvent, message=TextMessage)
def reverse_echo(event):
    # !Webhook設定 - 検証
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reverse_text = ''

        for i in event.message.text:

            reverse_text = i + reverse_text
            # print(reverse_text)

        # ▼ comeent out => debug
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reverse_text)
        )

if __name__ == "__main__":
    app.run()
