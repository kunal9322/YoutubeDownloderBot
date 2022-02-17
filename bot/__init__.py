# by <@kaif-00z>

import asyncio
import io
import sys
import time
import traceback

from yt_dlp import YoutubeDL
from telethon import Button, TelegramClient, errors, events
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

from .config import *

try:
    bot = TelegramClient(None, API_ID, API_HASH)
except Exception as e:
    print("Environment vars are missing")
    print(str(e))
    exit()
