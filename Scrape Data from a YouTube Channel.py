from bs4 import BeautifulSoup
import requests
import pandas as pd
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

def scrape_youtube_channel(channel_id):
    base_url = f"https://www.youtube.com/channel/{channel_id}/videos"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    video_titles = soup.find_all("a",{"class":"yt-simple-endpoint style-scope ytd-grid-video-renderer"})
    video_data = []
    for title in video_titles:
        video_data.append({"title": title["title"], "url": "https://www.youtube.com" + title["href"]})
    return video_data
def store_data_as_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
class Video(BaseModel):
    title: str
    url: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/videos/{channel_id}", response_model=List[Video])
def read_videos(channel_id: str):
    data = scrape_youtube_channel(channel_id)
    return data