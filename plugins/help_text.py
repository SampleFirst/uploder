import os
from config import Config
from translation import Translation
import logging
from pyrogram import filters, enums
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.adduser import AddUser

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )


@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source code ⚡", url="https://github.com/Clinton-Abraham/UPLOADER-BOT"),
                    InlineKeyboardButton("Project Channel 👨🏻‍💻", url="https://t.me/Space_X_bots"),
                ],
                [
                    InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/clinton_abraham")
                ],
            ]
        ),
    )
    
