"""
====================================================
Karen Voice Assistant
Configuration File
====================================================

This file stores all configurable values used
throughout the application.

Author : Pratyush
Project : Karen Voice Assistant
"""

from pathlib import Path
import logging

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "Karen Voice Assistant"
ASSISTANT_NAME = "Karen"
VERSION = "1.0.0"

# ==========================================================
# BASE DIRECTORIES
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"

# Create folders automatically if they don't exist
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# ==========================================================
# FILE PATHS
# ==========================================================

ASSISTANT_NAME_FILE = DATA_DIR / "assistant_name.txt"
LOG_FILE = LOG_DIR / "karen.log"

# ==========================================================
# TEXT TO SPEECH SETTINGS
# ==========================================================

VOICE_INDEX = 1      # 0 = Male, 1 = Female (depends on system)

VOICE_RATE = 150

VOICE_VOLUME = 1.0

# ==========================================================
# SPEECH RECOGNITION SETTINGS
# ====================================================== ====

LANGUAGE = "en-IN"

LISTEN_TIMEOUT = 5

PHRASE_TIME_LIMIT = 8

AMBIENT_NOISE_DURATION = 1

# ==========================================================
# USER DIRECTORIES
# ==========================================================

HOME_DIR = Path.home()

MUSIC_DIR = HOME_DIR / "Music"

PICTURES_DIR = HOME_DIR / "Pictures"

DOWNLOADS_DIR = HOME_DIR / "Downloads"

# ==========================================================
# SUPPORTED MUSIC FILES
# ==========================================================

SUPPORTED_AUDIO_FILES = (
    ".mp3",
    ".wav",
    ".aac",
    ".m4a",
    ".flac",
    ".ogg",
)

# ==========================================================
# WEBSITE LINKS
# ==========================================================

WEBSITES = {

    # Google
    "google": "https://www.google.com",

    # YouTube
    "youtube": "https://www.youtube.com",
    "yt": "https://www.youtube.com",

    # Facebook
    "facebook": "https://www.facebook.com",
    "fb": "https://www.facebook.com",

    # Instagram
    "instagram": "https://www.instagram.com",
    "insta": "https://www.instagram.com",

    # GitHub
    "github": "https://github.com",
    "git": "https://github.com",

    # Gmail
    "gmail": "https://mail.google.com",
    "mail": "https://mail.google.com",

    # LinkedIn
    "linkedin": "https://www.linkedin.com",
    "linked in": "https://www.linkedin.com",

    # Stack Overflow
    "stackoverflow": "https://stackoverflow.com",
    "stack overflow": "https://stackoverflow.com",

    # Reddit
    "reddit": "https://www.reddit.com",

    # ChatGPT
    "chatgpt": "https://chat.openai.com",
    "openai": "https://chat.openai.com",
}


# ==========================================================
# ENTITY CONFIGURATION
# ==========================================================

ENTITIES = {

    "website": WEBSITES,

}

# ==========================================================
# SCREENSHOT SETTINGS
# ==========================================================

SCREENSHOT_PREFIX = "Karen"

# ==========================================================
# TERMINAL SETTINGS
# ==========================================================

SHOW_USER_COMMAND = True
SHOW_ASSISTANT_RESPONSE = True

# ==========================================================
# LOGGING
# ==========================================================

ENABLE_LOGGING = True

LOG_LEVEL = logging.INFO

# ==========================================================
# NLP CONFIGURATION
# ==========================================================

STOP_WORDS = {

    "a",
    "an",
    "the",

    "can",
    "could",
    "would",
    "will",

    "please",
    "kindly",

    "you",
    "your",

    "me",
    "my",

    "to",
    "for",
    "of",
    "is",
    "are",
    "am"
}


INTENTS = {

    "open_website": {

        "open",
        "launch",
        "start",
        "visit",
        "go"

    },

    "play_music": {

        "play",
        "listen"

    },

    "wikipedia_search": {

        "search",
        "wikipedia",
        "who",
        "what"

    },

    "tell_time": {

        "time",
        "clock"

    },

    "tell_date": {

        "date",
        "day"

    },

    "take_screenshot": {

        "screenshot",
        "capture"

    },

    "tell_joke": {

        "joke",
        "funny"

    },

    "shutdown": {

        "shutdown",
        "poweroff"

    },

    "restart": {

        "restart",
        "reboot"

    },

    "exit": {

        "exit",
        "quit",
        "offline"

    }
}