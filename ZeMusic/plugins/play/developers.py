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
                
@app.on_message(filters.command(["مودي","المبرمج مودي","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮](https://t.me/elhyba)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @elhyba ❫
◉ 𝙸𝙳      : ❪ `6581896306` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@elhypa) my world (@Source_Ze - @up_uo) my bro (@e_l_z_o_u_z) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮", url=f"https://t.me/elhyba"), 
                 ],[
                   InlineKeyboardButton(
                        "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱", url=f"https://t.me/Source_Ze"),
                ],

            ]

        ),

    )
