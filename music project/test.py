from __future__ import unicode_literals
import yt_dlp
import sys

def my_hook(d):
    if d['status'] == 'downloading':
        print ("downloading "+ str(round(float(d['downloaded_bytes']))))
    if d['status'] == 'finished':
        filename=d['filename']
        print(filename)

ydl_opts = {
    'format': 'bestvideo[width<=1080]+bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'progress_hooks':[my_hook]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download("https://youtu.be/hCt-78kMx10")