# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
CHAT_ID = int(os.environ.get("CHAT_ID", 0))
Bot = Client(
    "Group-Chat-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Bot.on_message(filters.private & filters.all & filters.user(1607263889))
async def start(bot, update):
    await bot.send_message(CHAT_ID,update.text)
