import yt_dlp

class ZenAudioDownloader:
    """
    Zen Library: High-quality audio downloader module.
    """
    def __init__(self, output_path="."):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }

    def download(self, url):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
            return "Success: Audio downloaded."
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    downloader = ZenAudioDownloader()
    link = input("Enter Audio URL: ")
    print(downloader.download(link))
