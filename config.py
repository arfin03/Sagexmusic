import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","unfav_sage")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "sagexmusicbot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "Alone Music")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "AloneXHelper")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6699471415))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Sagexdd/Sagexmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sagebotsupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/unfav_sage")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://telegra.ph/file/a4202cc695daeb69fbc46.jpg", "https://telegra.ph/file/e1ce2335d309a74a060fb.jpg", "https://telegra.ph/file/de78daf84b6e6c4653279.jpg"]
PING_IMG_URL = ["https://telegra.ph/file/2d0d53df84d71af01c36a.jpg", "https://telegra.ph/file/ccd472a60ab35013c50f4.jpg", "https://telegra.ph/file/7d603abd5450fe81610d3.jpg"] 
STATS_IMG_URL = "https://telegra.ph/file/da59108812e9a8e5cee1f.jpg"
PLAYLIST_IMG_URL = "https://telegra.ph/file/b4546546b614b0c09b44d.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/b18708ec9238442461ab1.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/f5312b5be8f360398bdc4.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/9261fb5150e3d525d9d9f.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/4ab71a988a22e457dd828.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/2c3277327ed86d5e8969b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/de78daf84b6e6c4653279.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/7d603abd5450fe81610d3.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/7d603abd5450fe81610d3.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
