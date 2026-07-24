"""
Simple YouTube downloader using yt-dlp.

Install dependency first:
    pip install yt-dlp

Usage:
    python youtube_downloader.py
    (then paste a URL when prompted)

Or from the command line:
    python youtube_downloader.py "https://www.youtube.com/watch?v=XXXXXXXXXXX"
"""

import sys
import yt_dlp


def download_video(url: str, output_dir: str = "downloads", audio_only: bool = False,
                   subs_only: bool = False, proxy: str | None = None,
                   subtitles: bool = False, sub_langs: str = "en"):
    """
    Download a YouTube video, audio, or subtitles using yt-dlp.

    Args:
        url: The YouTube video URL.
        output_dir: Folder to save the file into.
        audio_only: If True, extract audio only (as mp3).
        subs_only: If True, download subtitles ONLY and skip the media.
        proxy: Optional proxy URL, e.g. "socks5://127.0.0.1:1080".
        subtitles: If True, download subtitles alongside the video/audio.
        sub_langs: Comma-separated language codes, e.g. "en,es,fr", or "all".
    """
    ydl_opts = {
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "progress_hooks": [progress_hook],
    }

    if proxy:
        ydl_opts["proxy"] = proxy

    # Subtitles configuration
    if subtitles or subs_only:
        ydl_opts.update({
            "writesubtitles": True,       # human-made subtitles, if available
            "writeautomaticsub": True,    # fall back to YouTube's auto-generated captions
            "subtitleslangs": sub_langs.split(","),
            "subtitlesformat": "srt/best",
        })

    # If the user wants ONLY subtitles, we skip downloading the video/audio streams entirely
    if subs_only:
        ydl_opts.update({
            "skip_download": True,
        })
    elif audio_only:
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
    else:
        # Best video+audio combined, capped at 1080p to keep things reasonable
        ydl_opts["format"] = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "video")
        print(f"\n✅ Done: {title}")


def progress_hook(d):
    if d["status"] == "downloading":
        pct = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "").strip()
        print(f"\rDownloading... {pct} at {speed}", end="", flush=True)
    elif d["status"] == "finished":
        print("\nProcessing...")


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter YouTube URL: ").strip()

    # Updated choice to include 's' for subtitles only
    choice = input("Download (v)ideo, (a)udio only, or (s)ubtitles only? [v/a/s]: ").strip().lower()

    audio_only = choice == "a"
    subs_only = choice == "s"

    proxy = input("Proxy URL (leave blank if none): ").strip() or None

    # Handle subtitle configurations
    if subs_only:
        subtitles = True  # Must be True to trigger writing them
        sub_langs = input("Subtitle language code(s) to download, comma-separated [en]: ").strip() or "en"
    else:
        sub_choice = input("Download subtitles too? [y/N]: ").strip().lower()
        subtitles = sub_choice == "y"
        sub_langs = "en"
        if subtitles:
            sub_langs = input("Subtitle language code(s), comma-separated [en]: ").strip() or "en"

    download_video(
        url,
        audio_only=audio_only,
        subs_only=subs_only,
        proxy=proxy,
        subtitles=subtitles,
        sub_langs=sub_langs
    )


if __name__ == "__main__":
    main()