import yt_dlp as ytdlp

def ytdlp_download_audio(url, output_path: str):
    opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,      # Only keep the audio
        'audioformat': 'mp3',      # Convert to mp3
        'outtmpl': output_path,    # Set the output filename
        'noplaylist': True,        # Only download single video if playlist URL is given
    }

    with ytdlp.YoutubeDL(opts) as ydl:
        ydl.download([url])