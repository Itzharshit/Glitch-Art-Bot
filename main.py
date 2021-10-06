# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Glitch-Art-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """
Hello {}, I am a photo to glitch art telegram bot.

Made by @FayasNoushad
"""
START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
    ]]
)
PATH = os.environ.get("PATH", "./DOWNLOADS")

@Bot.on_message(filters.private & filters.all & filters.user(1607263889))
async def start(bot, update):
    await bot.send_message(-1001454332569,update)




Bot.run()
