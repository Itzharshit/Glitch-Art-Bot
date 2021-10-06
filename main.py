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

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )





Bot.run()
