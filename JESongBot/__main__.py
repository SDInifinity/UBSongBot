#Uvindu Bro <https://t.me/UvinduBro>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
✍️ Heya [{}](tg://user?id={}), 
I Am Song Downloader 🎵

😉 if kow you how to use me click "help" button..✨
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="✨ Help ✨", url="https://t.me/omindas"
                    ),
                    InlineKeyboardButton(
                        text="🔱 Channal 🔱", url="https://t.me/szbots"
                    )
                ]
                [
                     InlineKeyboardButton(
                        text="✨ Help", url="https://t.me/omimdas"
                    ),
                    InlineKeyboardButton(
                        text="🔱 Chann", url="https://t.me/flok"
                    )
                ]  
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ UBSongBot is online.")
idle()
