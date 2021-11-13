# Author: pyrogrammers (https://github.com/pyrogrammer-s) (@pyrogrammer-s)
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
CHAT_ID = int(os.environ.get("CHAT_ID", 0))
Bot = Client(
    "Glitch-Art-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text(
        "**Welcome to group chat bot created by @pyrogrammers.**\n\n"
        "Using this bot you can send messeges to group anonymously using bots.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Join Channel", url="https://t.me/pyrogrammers"),
             InlineKeyboardButton("Join Channel", url="https://t.me/pyrogrammerschat")],
            [InlineKeyboardButton("Youtube channel", url="https://youtube.com/")]
        ])
    )
PATH = os.environ.get("PATH", "./DOWNLOADS")

@Bot.on_message(filters.private & filters.all & filters.user(1607263889))
async def start(bot, update):
    await bot.send_message(CHAT_ID,update.text)




Bot.run()
