
# YouTube Audio & Video Downloader (English)

This Python script allows you to download YouTube videos and audio in various formats. You can choose to download the audio as MP3, WAV, or other formats, and videos in MP4 with H.264 video and AAC audio codecs.

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
- **Open Audio Folder (open -a)**: Open the folder where audio files are saved. (If folder not found Try download video or audio first)
- **Open Video Folder(open -v)**: Open the folder where video files are saved.  (If folder not found Try download video or audio first)
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

# โปรแกรมดาวน์โหลดเสียงและวิดีโอจาก YouTube (ไทย)

สคริปต์ Python นี้ช่วยให้คุณดาวน์โหลดวิดีโอและเสียงจาก YouTube ในหลายรูปแบบ คุณสามารถเลือกดาวน์โหลดเสียงเป็น MP3, WAV หรือรูปแบบอื่น ๆ และดาวน์โหลดวิดีโอเป็น MP4 พร้อมด้วยโค้ด H.264 และเสียงแบบ AAC

## คุณสมบัติ

- ดาวน์โหลดเสียงจาก YouTube ในรูปแบบต่าง ๆ (MP3, WAV, OGG, AAC ฯลฯ)
- ดาวน์โหลดวิดีโอ YouTube พร้อมโค้ดวิดีโอ H.264 และเสียงแบบ AAC
- แปลงเสียงที่ดาวน์โหลดเป็นรูปแบบที่คุณต้องการ
- ทำความสะอาดชื่อไฟล์โดยอัตโนมัติเพื่อให้รองรับกับทุกแพลตฟอร์ม
- อินเทอร์เฟซใช้งานง่ายสำหรับดาวน์โหลดเสียงหรือวิดีโอ
- รองรับการดาวน์โหลดโดยตรงไปยังโฟลเดอร์ที่ระบุ

## ข้อกำหนดเบื้องต้น

- Python 3.6 ขึ้นไป
- ไลบรารี `yt-dlp` สำหรับดาวน์โหลดวิดีโอและเสียงจาก YouTube
- ไลบรารี `pydub` สำหรับการแปลงรูปแบบเสียง
- **FFmpeg** สำหรับการประมวลผลเสียงและวิดีโอ (ติดตั้งผ่าน `pydub`)

## การติดตั้ง

1. Clone repository นี้หรือดาวน์โหลดสคริปต์

2. ติดตั้งไลบรารีที่จำเป็น:
    ```bash
    pip install yt-dlp pydub
    ```

3. ตรวจสอบให้แน่ใจว่าคุณติดตั้ง **FFmpeg** ในระบบของคุณแล้ว หากยังไม่ได้ติดตั้ง ให้ดาวน์โหลดจาก [เว็บไซต์ FFmpeg](https://ffmpeg.org/download.html) และทำตามคำแนะนำ

4. รันสคริปต์:
    ```bash
    python downloader.py
    ```

## วิธีใช้งาน

เมื่อรันสคริปต์ คุณจะได้รับคำแนะนำให้ป้อน URL ของวิดีโอ YouTube และเลือกว่าจะดาวน์โหลดเสียงหรือวิดีโอ

### ตัวเลือกที่มีให้:
- **Audio (a)**: ดาวน์โหลดเสียงในรูปแบบที่คุณต้องการ (MP3, OGG, WAV, AAC ฯลฯ)
- **Video (v)**: ดาวน์โหลดวิดีโอในรูปแบบ MP4 พร้อมโค้ด H.264 และเสียงแบบ AAC
- **Open Audio Folder (open -a)**: เปิดโฟลเดอร์ที่เก็บไฟล์เสียง (หากไม่สามารถเปิดได้ ให้ลองดาวโหลดวิดีโอ หรือเสียงก่อน)
- **Open Video Folder (open -v)**: เปิดโฟลเดอร์ที่เก็บไฟล์วิดีโอ (หากไม่สามารถเปิดได้ ให้ลองดาวโหลดวิดีโอ หรือเสียงก่อน)
- **Exit (e)**: ออกจากโปรแกรม

### ตัวอย่างการใช้งาน:
1. รันสคริปต์:
    ```bash
    python downloader.py
    ```
2. ป้อน URL ของวิดีโอ YouTube:
    ```
    (YMC) Enter the YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```
3. เลือกรูปแบบการดาวน์โหลด:
    ```
    Do you want to download audio(a) or video(v)? (a/v): a
    ```
4. ระบุรูปแบบเสียงที่ต้องการ (เช่น `mp3`):
    ```
    Enter the desired audio format (mp3, ogg, wav, aac, flac, m4a): mp3
    ```

โปรแกรมจะดาวน์โหลดและแปลงไฟล์เสียงเป็นรูปแบบที่คุณต้องการ หากเลือกดาวน์โหลดวิดีโอ จะดาวน์โหลดในรูปแบบ MP4

## ฟังก์ชัน

### `download_audio(url, format='mp3', output_folder='C:\\ydl\\Audio')`
ดาวน์โหลดเสียงจาก URL ของ YouTube ที่กำหนด และแปลงเป็นรูปแบบที่ระบุ

### `download_video(url, output_folder='C:/ydl/Video')`
ดาวน์โหลดวิดีโอและเสียงจาก YouTube ในรูปแบบ MP4 พร้อมโค้ดวิดีโอ H.264 และเสียงแบบ AAC

## โครงสร้างโฟลเดอร์

- **Audio folder**: เก็บไฟล์เสียงที่ดาวน์โหลด (ค่าเริ่มต้นคือ `C:/ydl/Audio`)
- **Video folder**: เก็บไฟล์วิดีโอที่ดาวน์โหลด (ค่าเริ่มต้นคือ `C:/ydl/Video`)

## การแก้ไขปัญหา

- **FFmpeg not found**: หากโปรแกรมทำงานไม่ได้เพราะหา FFmpeg ไม่เจอ ตรวจสอบให้แน่ใจว่าได้ติดตั้ง FFmpeg แล้วและสามารถเข้าถึงได้จาก PATH ของระบบ
"""
  
