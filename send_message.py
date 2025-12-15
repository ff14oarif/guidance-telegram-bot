import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
MESSAGE = "📢 매일 정해진 시간에 보내는 자동 메시지입니다!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

requests.post(url, data=data)
