import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

MESSAGE = """
📢 일일 공지

죄인명단:
- <a href="tg://user?id=5533645995">벨워터</a>
- <a href="tg://user?id=5645992843">스게</a>
- <a href="tg://user?id=5650466481">카벤디아</a>

가이던스 공용 캘린더 권한 주기 위한 구글 아이디 다오
요 없으면 안 줘도 되고 나중에 줘도 됨
예 아니오 답을 안 주면 줄 때까지 말 걸 거임(공산품이 거는겁니다 오아리프가 고생할까봐 걱정하지 않으셔도 됩니다)
이 알람은 매일 주겠습니다.
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": MESSAGE,
    "parse_mode": "HTML"
}

requests.post(url, data=data)
