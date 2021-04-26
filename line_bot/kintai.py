from flask import Flask, request, abort
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi, WebhookHandler
)
import pandas as pd
from datetime import datetime, timedelta, timezone
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')
SP_CREDENTIAL_FILE = 'secret.json'
SP_SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

SP_SHEET_KEY = 'SP_SHEET_KEY'
SP_SHEET = 'SP_SHEET'
app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('YOUR_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('YOUR_CHANNEL_SECRET'))


def auth():
    """認証
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SP_CREDENTIAL_FILE,
        SP_SCOPE
    )
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

def punch_in():
    """出勤
    """
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now(JST)
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in,
                    '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

def punch_out():
    """退勤
    """
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now(JST)
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

@app.route("/callback", methods=["GET", "POST"])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '出勤':
        punch_in()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="出勤登録完了しました！今日もがんばりましょう！"))
    elif event.message.text == '退勤':
        punch_out()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="退勤登録完了しました！お疲れ様でした"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="こちらは出退勤を管理するBotです。"))


if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(host="0.0.0.0", port=port)
