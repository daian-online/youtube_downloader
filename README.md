# YouTube Downloader

A simple YouTube downloader built with **Python** and **yt-dlp**.

It can download:

- 🎥 Videos (up to 1080p)
- 🎵 Audio only (MP3)
- 💬 Subtitles only
- 🎥 Videos with subtitles
- 🎵 Audio with subtitles
- 🌐 Downloads through an HTTP/SOCKS proxy

---

## Requirements

- Python 3.10 or newer
- FFmpeg (required for audio conversion to MP3)
- `yt-dlp`

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

Or simply download the project files.

### 2. Install yt-dlp

```bash
pip install yt-dlp
```

### 3. Install FFmpeg

FFmpeg is required when downloading audio as MP3.

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

#### Arch Linux

```bash
sudo pacman -S ffmpeg
```

#### Fedora

```bash
sudo dnf install ffmpeg
```

#### Windows

Download FFmpeg from:

https://ffmpeg.org/download.html

Add it to your system PATH.

---

## Usage

Run the script:

```bash
python youtube_downloader.py
```

or provide the URL directly:

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## Interactive Prompts

After starting the program, you'll be asked several questions.

### 1. Enter the YouTube URL

Example:

```
Enter YouTube URL:
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

---

### 2. Choose what to download

```
Download (v)ideo, (a)udio only, or (s)ubtitles only? [v/a/s]:
```

Options:

| Option | Description |
|---------|-------------|
| `v` | Download the video |
| `a` | Download audio only (MP3) |
| `s` | Download subtitles only |

---

### 3. Proxy (optional)

```
Proxy URL (leave blank if none):
```

Examples:

HTTP proxy

```
http://127.0.0.1:8080
```

SOCKS5 proxy

```
socks5://127.0.0.1:1080
```

Leave blank if you don't use a proxy.

---

### 4. Subtitles

If you selected **video** or **audio**, you'll be asked:

```
Download subtitles too? [y/N]:
```

If you answer **y**, enter one or more language codes:

```
Subtitle language code(s), comma-separated [en]:
```

Examples:

English

```
en
```

English + Spanish

```
en,es
```

All available subtitles

```
all
```

---

If you selected **subtitles only**, you'll only be asked for the subtitle language.

---

## Output

Downloaded files are saved in the `downloads/` directory.

Example:

```
downloads/
├── My Video.mp4
├── My Video.mp3
├── My Video.en.srt
└── Another Video.es.srt
```

---

## Examples

### Download a video

```
Enter YouTube URL:
https://youtu.be/VIDEO_ID

Download (v)ideo, (a)udio only, or (s)ubtitles only? [v/a/s]:
v

Proxy URL:
<leave blank>

Download subtitles too? [y/N]:
n
```

---

### Download audio as MP3

```
Download (v)ideo, (a)udio only, or (s)ubtitles only? [v/a/s]:
a
```

---

### Download subtitles only

```
Download (v)ideo, (a)udio only, or (s)ubtitles only? [v/a/s]:
s

Subtitle language:
any subtitle language available in youtube for example:
en -> English
fa -> Farsi(Persian)
fr -> French
```

---

## Features

- Download videos up to **1080p**
- Extract audio as **MP3**
- Download subtitles in one or multiple languages
- Supports auto-generated subtitles if manual subtitles are unavailable
- Supports HTTP and SOCKS proxies
- Displays download progress
- Saves files using the original YouTube title

---

## Notes

- Some videos may not have subtitles available.
- If manually created subtitles don't exist, the program attempts to download YouTube's auto-generated subtitles.
- Audio conversion requires FFmpeg to be installed and available in your system PATH.
- Download speeds depend on your internet connection and YouTube availability.

---

## Dependencies

- Python 3.10+
- yt-dlp
- FFmpeg

Install Python package:

```bash
pip install yt-dlp
```


### Install FFmpeg

Audio extraction to MP3 requires FFmpeg.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify the installation:

```bash
ffmpeg -version
```
---

## License

This project is provided as-is for educational and personal use.
