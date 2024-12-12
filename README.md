# Youtube-URL-Downloader
Download youtube video with python yt-dlp

## Features

- Download audio from YouTube in various formats (MP3, WAV, OGG, AAC, etc.).
- Download YouTube videos with the H.264 video codec and AAC audio codec.
- Converts downloaded audio to your chosen format if needed.
- Automatically sanitizes file names to ensure compatibility across platforms.
- Easy-to-use interface for downloading audio or video.
- Supports downloading directly into a specified folder.

## Requirements

- Python 3.6+
- `yt-dlp` for downloading YouTube videos and audio.
- `pydub` for audio format conversion.
- `ffmpeg` is required for audio and video processing (installed via `pydub`).

## Installation

1. Clone this repository or download the script.

2. Install the required libraries:
    ```bash
    pip install yt-dlp pydub
    ```

3. Make sure you have **FFmpeg** installed on your system. If you don't, download it from [FFmpeg's website](https://ffmpeg.org/download.html) and follow the installation instructions.

4. Run the script:
    ```bash
    python downloader.py
    ```

## Usage

Upon running the script, you will be prompted to input the URL of the YouTube video and select whether you want to download the audio or video.

### Available options:
- **Audio (a)**: Download audio in your desired format (MP3, OGG, WAV, AAC, etc.).
- **Video (v)**: Download the video in MP4 format with H.264 and AAC audio.
- **Open Audio Folder (open -a)**: Open the folder where audio files are saved.
- **Open Video Folder(open -v)**: Open the folder where video files are saved.
- **Exit (e)**: Exit the program.

### Example:
1. Run the script:
    ```bash
    python downloader.py
    ```
2. Enter the YouTube URL:
    ```
    (YMC) Enter the YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```
3. Choose the download mode:
    ```
    Do you want to download audio(a) or video(v)? (a/v): a
    ```
4. Specify the desired audio format (e.g., `mp3`):
    ```
    Enter the desired audio format (mp3, ogg, wav, aac, flac, m4a): mp3
    ```

The script will download the audio and convert it into the desired format. If a video is chosen, it will download the video in MP4 format.

## Functions

### `download_audio(url, format='mp3', output_folder='C:\\ydl\\Audio')`
Downloads audio from the given YouTube URL and converts it to the specified format.

### `download_video(url, output_folder='C:/ydl/Video')`
Downloads the video and audio from YouTube in MP4 format with H.264 video and AAC audio codecs.


## Folder Structure

- **Audio folder**: Where downloaded audio files are stored (default is `C:/ydl/Audio`).
- **Video folder**: Where downloaded video files are stored (default is `C:/ydl/Video`).

## Troubleshooting

- **FFmpeg not found**: If the script does not work because it can't find FFmpeg, ensure that FFmpeg is installed and accessible from your system's PATH.
