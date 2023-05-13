import yt_dlp


def download():
    
	video_url = input("Enter URL: ")
	video_info = yt_dlp.YoutubeDL().extract_info(url=video_url, download = False)
	file = f"{video_info['title']}.mp3"
	options={
		'format':'bestvideo+bestaudio'
	}
	with yt_dlp.YoutubeDL(options) as ydl:
		ydl.download([video_info['webpage_url']])


download()