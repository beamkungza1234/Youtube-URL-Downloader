import re
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def sanitize_filename(filename):
    # Replace invalid characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_audio(url, format='mp3', output_folder='C:\\ydl\\Audio'):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Validate format
    valid_formats = ['mp3', 'ogg', 'wav', 'aac', 'flac', 'm4a']
    if format not in valid_formats:
        raise ValueError(f"Format must be one of {', '.join(valid_formats)}")
    
    # Download the audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # Temporary wav format
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = sanitize_filename(info_dict.get('title', None))
        out_file = os.path.join(output_folder, f"{title}.wav")

    # Convert to specified format if it's not already WAV
    if format != 'wav':
        new_file = os.path.join(output_folder, f"{title}.{format}")
        audio = AudioSegment.from_file(out_file)
        audio.export(new_file, format=format)

        # Remove the temporary WAV file
        os.remove(out_file)
        print(f"{title} has been successfully downloaded and converted to {format}.")
    else:
        new_file = out_file
        print(f"{title} has been successfully downloaded in WAV format.")

    return new_file

def download_video(url, output_folder='C:/ydl/Video'):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Specify format to force H.264 for video and AAC for audio
    ydl_opts = {
        'format': 'bestvideo[vcodec^=avc1]+bestaudio[acodec^=mp4a]/mp4',  # Force H.264 (avc1) for video and AAC (mp4a) for audio
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',  # Merge output as MP4
        'postprocessor_args': [
            '-c:v', 'libx264',  # Re-encode video to H.264 (if needed)
            '-c:a', 'aac',      # Re-encode audio to AAC
            '-b:a', '192k',     # Set audio bitrate to 192kbps
        ]
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = sanitize_filename(info_dict.get('title', None))
        new_file = os.path.join(output_folder, f"{title}.mp4")

    print(f"{title} has been successfully downloaded as an MP4 video with H.264 and AAC audio.")
    return new_file


def donext():
    url = input("(YMC) Enter the YouTube URL: ")
    mode = input("Do you want to download audio(a) or video(v)? (a/v)\nOr open downloaded folder (open -a/open -v): ").lower()

    if mode == 'a':
        format = input("Enter the desired audio format (mp3, ogg, wav, aac, flac, m4a): ").lower()
        download_audio(url, format)
    elif mode == 'v':
        download_video(url)
    elif mode == 'e':
        exit()
    elif mode == 'open -a':
        print("Opening Audio folder...")
        os.startfile(r'C:\ydl\Audio')
        print("Open Audio folder >>")
    elif mode == 'open -v':
        print("Opening Video folder...")
        os.startfile(r'C:\ydl\Video')  
        print("Open video folder >>")  
    else:
        print("Invalid mode selected. Please choose 'audio(a)' or 'video(v)'.")

# Main loop to keep the script running
while True:
    donext()
