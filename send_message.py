import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
MESSAGE = "<a href="tg://user?id=5533645995">@벨워터</a>, <a href="tg://user?id=5645992843">스게</a>, <a href="tg://user?id=5650466481">카벤디아</a> \n \n 가이던스 공용 캘린더 권한 주기 위한 구글 아이디 다오 \n \n 필요없으면 안줘도 되고 나중에 줘도 됨 \n \n 예 아니오 답을 안주면 줄떄까지 말걸거임
갠텔로 줘도 됨 \n \n 이 알람은 매일 주겠습니다."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

requests.post(url, data=data)
