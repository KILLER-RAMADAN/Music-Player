import yt_dlp
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info('https://youtu.be/g3pTnK6jRfo', download=False)
    video_title = info_dict.get('title', None)
    # if video_title:
        # print(f'Video title: {video_title}')
    ydl.download(['https://youtu.be/g3pTnK6jRfo'])