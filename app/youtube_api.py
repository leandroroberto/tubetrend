import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API")

YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"

def buscar_videos(palavra_chave, max_results=10):

    url = f"{YOUTUBE_API_URL}/search"
    
    params = {
        "part": "snippet",
        "q" : palavra_chave,
        "type" : "video",
        "maxResults" : max_results,
        "key" : API_KEY,
        "order" : "viewCount",
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"erro" : response.text}
