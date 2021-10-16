# by <@kaif-00z>

from telethon import Button, TelegramClient, errors, events
import asyncio
import sys
import io
import time
import traceback
import youtube_dl

from .config import *


try:
    bot = TelegramClient(None, API_ID, API_HASH)
except Exception as e:
    print("Environment vars are missing")
    print(str(e))
    exit()
