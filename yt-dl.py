# pip install yt-dlp
import yt_dlp

def download_playlist(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

playlist_url = 'https://youtube.com/playlist?list=PLPdN9Po1toQyZ-F1A_yHQqA3UHZD9NYOX&si=6Oc24Myd_wPJQmZi'
download_playlist(playlist_url)
