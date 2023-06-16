# Import the required modules
import os
import random
import requests
import moviepy.editor as mpe
from gtts import gTTS

# Set the variables
title = "How to create a TikTok video using Python"
script = "Hello, in this video I will show you how to create a TikTok video using Python. You will need to install some modules and write some code. Let's get started."
keyword = "python"

# Search for videos using the Pexels API
api_key = "your_api_key" # replace with your own API key
url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=10"
headers = {"Authorization": api_key}
response = requests.get(url, headers=headers)
data = response.json()

# Save the videos to a folder called downloaded_videos
if not os.path.exists("downloaded_videos"):
os.mkdir("downloaded_videos")

for video in data["videos"]:
video_url = video["video_files"][0]["link"]
video_id = video["id"]
video_name = f"downloaded_videos/{video_id}.mp4"
r = requests.get(video_url)
with open(video_name, "wb") as f:
f.write(r.content)

# Choose a random video from a folder called intro_videos
intro_videos = os.listdir("intro_videos")
intro_video_name = random.choice(intro_videos)
intro_video_path = f"intro_videos/{intro_video_name}"

# Generate a text to speech audio file using the script variable
speech_audio = gTTS(text=script, lang="en")
speech_audio.save("speech_audio.mp3")

# Generate a text overlay using the title variable
text_clip = mpe.TextClip(title, fontsize=70, color="white", bg_color="black")
text_clip = text_clip.set_duration(5).set_position("center")

# Combine all the videos and audio and text overlay together into one 1080 x 1920 sized video
video_clips = []
video_clips.append(mpe.VideoFileClip(intro_video_path))
for video in os.listdir("downloaded_videos"):
video_path = f"downloaded_videos/{video}"
video_clips.append(mpe.VideoFileClip(video_path))
final_video = mpe.concatenate_videoclips(video_clips)
final_video = final_video.resize((1080, 1920))
final_video = final_video.set_audio(mpe.AudioFileClip("speech_audio.mp3"))
final_video = mpe.CompositeVideoClip([final_video, text_clip])
final_video.write_videofile("final_video.mp4")