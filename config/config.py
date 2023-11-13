import re

import sys

from os import getenv

from dotenv import load_dotenv

from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org

API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH", "")

## Get it from @Botfather in Telegram.

BOT_TOKEN = getenv("BOT_TOKEN", "")

# Database to save your chats and stats.

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.

DURATION_LIMIT_MIN = int(

    getenv("DURATION_LIMIT", "760")

)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot

SONG_DOWNLOAD_DURATION = int(

    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "360")

)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

# A name for your Music bot.

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","")

# Your User ID.

OWNER_ID = list(

    map(int, getenv("OWNER_ID", "").split())

)  # Input type must be interger

# Get it from http://dashboard.heroku.com/account

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# For customized or modified Repository

UPSTREAM_REPO = getenv(

    "UPSTREAM_REPO",

    "https://github.com/Pyaaditya/ZenMusic",

)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN ( if your edited repo is private)

GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.

SUPPORT_CHANNEL = getenv(

    "SUPPORT_CHANNEL", "https://t.me/ZenBotx") # Example:- https://t.me/ArchBots

SUPPORT_GROUP = getenv(

    "SUPPORT_GROUP", "https://t.me/QuirkySquad")  # Example:- https://t.me/ARCH_SUPPORTS

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "5400")

)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.

AUTO_SUGGESTION_TIME = int(

    getenv("AUTO_SUGGESTION_TIME", "5400")

)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command

GITHUB_REPO = getenv("GITHUB_REPO", None) 

# Spotify Client.. Get it from https://developer.spotify.com/dashboard

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "a8ff19344adb447bb4fe755f6f200a60")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "784a2fbead694c8bb928d499572dc70b")

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "10"))

# Maximum Limit Allowed for users to save playlists on bot's server

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

# Cleanmode time after which bot will delete its old messages from chats

CLEANMODE_DELETE_MINS = int(

    getenv("CLEANMODE_MINS", "3")

)  # Remember to give value in Seconds

# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(

    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")

)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(

    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")

)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.

# Refer to https://i.postimg.cc/Bbg3LQTG/image.png

SET_CMDS = getenv("SET_CMDS", False)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot

STRING1 = getenv("STRING_SESSION", "")

STRING2 = getenv("STRING_SESSION2", "BQAJorTv1KWUXXWzHMjB0EV0vvAYv6QQqrmzuidAmFg3ysqYPBVhI3gXWZ0U8fr5pwnDfayYUinSu-aEMSAznZ_FzzAVdGP4xchF0DIfFchXdM5-aR7MHDLsq-vbNntFKEjGiZ0S__RIKUqx-pAU_haKwEazsBBjkpbtRqGcCq5K41CiPILLSFuHVpXujOCPSYKdSlsd-1mMfqrsya5crd3a5SuJJ6F66GOjIR4mPMv5nMKzzk_nStlsg804kI4ZYbhz3ifEPOwrHNymedXz_9GndREhUt95DKirHWi4SstTKhPj_q7wsrL7-smHwFDOF49iLAlSXLRwO4e9ZnRRnxndAAAAAZ9lhUYA")

STRING3 = getenv("STRING_SESSION3", "BQBwL-NxVJAPwgdXO8ql6FLyKQ9tupdhhANNGCiNSmrs_W9gc3G5-zujsBzPf6uZtd3RzS4P8yYjlUzj_2CKXe54-kp0_zJ2bcBkByhWg1sZV8DlYTf0cA7uCqik1k4TO1k17Sv26475SUtV_nkJBnlcv7CA03GExk92LNpoSjPhSkS6gnoF7p1V8dZ9QPixJUVcqmQKexUYiKIVK44QVPyj-ddRj-Ajm72CeWttZ9vSthFhR87lhKtZS2_Cex_C5oTM1kEEQY_ytWHIWy58cPz8XSs0XiC9O0FCEKV8L9fmEhySFVT6mJbWwUQIWmpPwPbSJkB-9S7_xCSKtUGt3dsFAAAAAYM94KoA")

STRING4 = getenv("STRING_SESSION4", "BQDCYhIPRlrIjKU0otvXIraoR7Pzzlfj07LcayxsFR745RYrx2KYEwMUOGq87ILLu7g0tcunnd69cdlaY5QjScmrFz8c5aaPkP5ELQ6x2F-xk7v7Kgt8IDTx9ui63Rr8gHD8b85TIyInz06J_JaD3a6HfimxxowPZjQAgbjQN9Snzp_E7NAqjsOqhKFqKeLObmXL8jetH2BR_NTzP7caacWJdSHtPN2_NSRmzUwOQpRjO12LPWjzMsRknnHAtgVt4JFmcBDNCoOhQ7FcJ3w0bOihls2walCLrbN9BtDLbcweexzG7y1RHKpf1Q5Qg_GOIgQZ1d1O-4CXZ87fEEwEtiRrAAAAAZytQkoA", None)

STRING5 = getenv("STRING_SESSION5", None)

### DONT TOUCH or EDIT codes after this line

BANNED_USERS = filters.user()

YTDOWNLOADER = 1

LOG = 2

LOG_FILE_NAME = "ZenMusiclogs.txt"

adminlist = {}

lyrical = {}

chatstats = {}

userstats = {}

clean = {}

autoclean = []

# Images

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/ac428f25366157cafdd90.jpg")

PING_IMG_URL = getenv(

    "PING_IMG_URL",

    "assets/Ping.jpeg",

)

PLAYLIST_IMG_URL = getenv(

    "PLAYLIST_IMG_URL",

    "assets/Playlist.jpeg",

)

GLOBAL_IMG_URL = getenv(

    "GLOBAL_IMG_URL",

    "assets/Global.jpeg",

)

STATS_IMG_URL = getenv(

    "STATS_IMG_URL",

    "assets/Stats.jpeg",

)

TELEGRAM_AUDIO_URL = getenv(

    "TELEGRAM_AUDIO_URL",

    "assets/Audio.jpeg",

)

TELEGRAM_VIDEO_URL = getenv(

    "TELEGRAM_VIDEO_URL",

    "assets/Video.jpeg",

)

STREAM_IMG_URL = getenv(

    "STREAM_IMG_URL",

    "assets/Stream.jpeg",

)

SOUNCLOUD_IMG_URL = getenv(

    "SOUNCLOUD_IMG_URL",

    "assets/Soundcloud.jpeg",

)

YOUTUBE_IMG_URL = getenv(

    "YOUTUBE_IMG_URL",

    "assets/Youtube.jpeg",

)

SPOTIFY_ARTIST_IMG_URL = getenv(

    "SPOTIFY_ARTIST_IMG_URL",

    "assets/SpotifyArtist.jpeg",

)

SPOTIFY_ALBUM_IMG_URL = getenv(

    "SPOTIFY_ALBUM_IMG_URL",

    "assets/SpotifyAlbum.jpeg",

)

SPOTIFY_PLAYLIST_IMG_URL = getenv(

    "SPOTIFY_PLAYLIST_IMG_URL",

    "assets/SpotifyPlaylist.jpeg",

)

def time_to_seconds(time):

    stringt = str(time)

    return sum(

        int(x) * 60**i

        for i, x in enumerate(reversed(stringt.split(":")))

    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

SONG_DOWNLOAD_DURATION_LIMIT = int(

    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")

)

if SUPPORT_CHANNEL:

    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):

        print(

            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"

        )

        sys.exit()

if SUPPORT_GROUP:

    if not re.match("(?:http|https)://", SUPPORT_GROUP):

        print(

            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"

        )

        sys.exit()

if UPSTREAM_REPO:

    if not re.match("(?:http|https)://", UPSTREAM_REPO):

        print(

            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"

        )

        sys.exit()

if GITHUB_REPO:

    if not re.match("(?:http|https)://", GITHUB_REPO):

        print(

            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"

        )

        sys.exit()

if PING_IMG_URL:

    if PING_IMG_URL != "assets/Ping.jpeg":

        if not re.match("(?:http|https)://", PING_IMG_URL):

            print(

                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if PLAYLIST_IMG_URL:

    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":

        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):

            print(

                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if GLOBAL_IMG_URL:

    if GLOBAL_IMG_URL != "assets/Global.jpeg":

        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):

            print(

                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if STATS_IMG_URL:

    if STATS_IMG_URL != "assets/Stats.jpeg":

        if not re.match("(?:http|https)://", STATS_IMG_URL):

            print(

                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if TELEGRAM_AUDIO_URL:

    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":

        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):

            print(

                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if STREAM_IMG_URL:

    if STREAM_IMG_URL != "assets/Stream.jpeg":

        if not re.match("(?:http|https)://", STREAM_IMG_URL):

            print(

                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if SOUNCLOUD_IMG_URL:

    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":

        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):

            print(

                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if YOUTUBE_IMG_URL:

    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":

        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):

            print(

                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if TELEGRAM_VIDEO_URL:

    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":

        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):

            print(

                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if MUSIC_BOT_NAME.isascii():

    print(

        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."

    )

    sys.exit()
