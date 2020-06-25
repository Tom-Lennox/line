from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from pathlib import Path
from typing import List
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import ImageMessage
from linebot.models import ImageSendMessage

import atexit

THIS_REPO = "20200622_line_return_pic"
SOURCE_IMAGE_PATH = THIS_REPO + "/static/images/{}.jpg"
PRESERVED_IMAGE_PATH = "/static/images/{}.jpg"

# ▼ local
local_path = "https://a5f57ab94dd1.ngrok.io"
# static_path = "___brbrbrbbrbrbrbrbbrbrbrbrb___"

import configparser

app = Flask(__name__)

# ▼ env file loading
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

line_bot_api = LineBotApi(os.environ["YOUR_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["YOUR_CHANNEL_SECRET"])

# ▼ Connecting to the LINE Messaging API
# 【指定】${ ngrok url }/callback  ⇒ (LINE Dev)　Webhook
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("|||Request body: " + body)
    
    # parse webhook body
    try:
        print('|||body : ', body)
        print('|||signature : ', signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# ▼ text manipulation
@handler.add(MessageEvent, message=TextMessage)
def reverse_echo(event):
    # !Webhook設定 - 検証
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        print("|||event", event)
        reverse_text = '※This account only accepts submission of images.'

        # ▼ comeent out => debug
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reverse_text)
        )

# ▼ image return
@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    message_id = event.message.id

    source_image_path = Path(SOURCE_IMAGE_PATH.format(message_id)).absolute()
    preserved_image_path = PRESERVED_IMAGE_PATH.format(message_id)

    print("|||event", event)
    print("|||source_image_path", source_image_path)
    print("|||preserved_image_path", preserved_image_path)
    
    # ▼ save image
    save_image(message_id, source_image_path)

    # ▼ send image
    # I feel it's a bad idea to specify a 3rd argument.
    # send_messagae(message_id, preserved_image_path, event).start()
    # send_messagae(message_id, preserved_image_path, event).join()
    send_messagae(message_id, preserved_image_path, event)

    # ▼ del picture
    atexit.del_picture(source_image_path)

def public_attr(obj) -> List[str]:
    return [x for x in obj.__dir__() if not x.startswith("_")]


def save_image(message_id: str, save_path: str) -> None:
    message_content = line_bot_api.get_message_content(message_id)
    with open(save_path, "wb") as f:
        for chunk in message_content.iter_content():
            f.write(chunk)

def send_messagae(message_id: str, preserved_image_path: str, event: str):
    image_message = ImageSendMessage(
        original_content_url = local_path + preserved_image_path,
        preview_image_url = local_path + preserved_image_path
    )

    line_bot_api.reply_message(
        event.reply_token,
        image_message
    )

def del_picture(source_image_path):
    source_image_path.unlink()
    os.remove(source_image_path)

if __name__ == "__main__":
    app.run()
