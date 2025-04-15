import yt_dlp

url = 'https://www.youtube.com/watch?v='

ydl_opts = {
    'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a][acodec^=mp4a]/best[ext=mp4][vcodec^=avc1]',
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    'restrictfilenames': True,
    'cookiesfrombrowser': ('chrome',),
}



with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
