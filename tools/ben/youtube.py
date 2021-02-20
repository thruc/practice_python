from apiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',  # 検索したい文字列を指定
    q='ボードゲーム',
    order='viewCount',  # 視聴回数が多い順に取得
    type='video',
).execute()

print(search_response["items"])
