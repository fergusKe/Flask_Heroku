# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('DVhOUDsodBZKg5Aiolyox+mPtB4/O4Gsuo9eh9B1c7Z9r2u4g/3tNxoXCEA8uKKYE6NyVXAPWbXd9HzIsLOg/RREFYBKzKJAm1rM2bewgGAe991grswCSOFW89niqywqZIr+c6o2z7ZHtBKSHIxr0QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ec95ecb53834da2fbd5b9f2928263a50')



@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)
