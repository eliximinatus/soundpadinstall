import os
import yt_dlp
import argparse
import webbrowser
import time
import subprocess

ffmpeg = False
ffprobe = False

parser = argparse.ArgumentParser(description="Hi")
parser.add_argument("url", type=str, default='N/A', help="The link to the video (or sound) you'd like to download", nargs=1)

curdir = os.listdir()
for stuff in curdir:
    if stuff.startswith('ffmpeg'):
        ffmpeg = True
    if stuff.startswith('ffprobe'):
        ffprobe = True

if ffmpeg == False or ffprobe == False:
    if ffmpeg == False:
        print("ffmpeg is not found in the current directory, please install!")
    if ffprobe == False:
        print("ffprobe is not found in the current directory, please install!")
    exit()

args = parser.parse_args()
url = args.url
if isinstance(url, list):
    url = url[0]

if url ==  "N/A":
    print('Please enter a URL!')
    exit()

def download_video(link):
    ytopt = {
        'outtmpl': f'./SOUNDPADINSTALL.%(title)s.%(ext)s',
        'youtube:player_client':'tv_embedded',
        #'format': 'bestaudio',
        'quiet': True,          
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",  # Use FFmpeg to extract audio
                "preferredcodec": "mp3",     # Convert to MP3
                "preferredquality": "192",   # Set desired audio quality (e.g., 192kbps)
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ytopt) as ytdl:
            print('Attempting download...')
            ytdl.download([link])
        print('Downloaded!')

    except Exception as error:
        print(f"Downloading \"{link}\" failed: {error}")
        exit()

download_video(url)

dir = os.listdir()




deathmark = []

# wait for ffmpeg conversion
time.sleep(5)

for file in dir:
    if file.startswith('SOUNDPADINSTALL.'):
        os.rename(file, file.removeprefix('SOUNDPADINSTALL.'))
        time.sleep(1)
        print(f'Found {file}')
        deathmark.append(file.removeprefix('SOUNDPADINSTALL.'))
        
try:
    server = subprocess.Popen('python -m http.server 45993')
    for markedfordeath in deathmark:
        webbrowser.open(f'soundpad://sound/url/https://localhost:45993/{markedfordeath}')
        time.sleep(3)
        os.remove(markedfordeath)
        # wait for soundpad import
    time.sleep(5)
finally:
    server.kill()





print('Done!')
print('Exiting...')


