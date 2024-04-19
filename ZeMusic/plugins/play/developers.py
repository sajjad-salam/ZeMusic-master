import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["باشه","المبرمج","مبرمج السورس","المالك"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/522d508e2bcb1db660111.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[الـبـاشـة ](https://t.me/G_D_U)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @G_D_U ❫
◉ 𝙸𝙳      : ❪ `733756075` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@G_D_U) my world (@G_D_U_VIP - @N_9_N_6)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒الـبـاشـة", url=f"https://t.me/G_D_U"), 
                 ],[
                   InlineKeyboardButton(
                        "الـبـاشـة", url=f"https://t.me/G_D_U_VIP"),
                ],

            ]

        ),

    )
