"""
MIT License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022 Hodacka
Copyright (c) 2022, Yūki • Black Knights Union, <https://github.com/Hodacka/AeroRobot-3>
This file is part of @Aero_Management_Bot (Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Software), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from telethon import events, Button, custom
import re, os
from AeroRobot.events import register
from AeroRobot import telethn as tbot
from AeroRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/a21731c0c4c7f27a3ec16.jpg"
@register(pattern=("/alive"))
async def awake(event):
  AERODYNAMIC = f"**♡ hey {event.sender.first_name} I,m Aerodynamic Robot** \n\n"
  AERODYNAMIC += "**♡ I'm Working with Cuteness**\n\n"
  AERODYNAMIC += "**♡ Aerodynamic: LATEST Version**\n\n"
  AERODYNAMIC += "**♡ My Creator:** [AerodynamicV1_OFFICIAL](t.me/AerodynamicV1_OFFICIAL)\n\n"
  AERODYNAMIC += "**♡ python-Telegram-Bot: 13.11**\n\n"
  BUTTON = [[Button.url("🚑 Support", "https://t.me/AerodynamicV1_Promotion"), Button.url("📢 Updates", "https://t.me/AerodynamicV1_UPDATE")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=AERODYNAMIC,  buttons=BUTTON)
