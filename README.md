This is a simple, lightweight Python script to automate downloading sound files from YouTube, BiliBili, and any other supported sites, and installing them to Soundpad.
# Explanation

This script downloads the file with the prefix "SOUNDPADINSTALL.", looks for each and every file with that same prefix in the current directory, adds it to a list, hosts the directory on localhost, then runs "```soundpad://sound/url/https://localhost:45993/FileName```"
# Dependencies
You need [ffmpeg + ffprobe](https://ffmpeg.org/) in the script's directory, or the directory you're running it in, and [yt_dlp](https://github.com/yt-dlp/yt-dlp)

Run `pip install yt_dlp` in your terminal, or `./bin/pip install yt_dlp` if you're using a VENV

ffmpeg can be installed through your distro's package manager, or through the links provided above.




