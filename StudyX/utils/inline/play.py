import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, YOUR_GROUP, YOUR_CHANNEL
from StudyX import app

import config
from StudyX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    Study = math.floor(percentage)
    if 0 < Study <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < Study < 3:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= Study < 4:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= Study < 5:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= Study < 7:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= Study < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= Study < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= Study < 12:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= Study < 13:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < Study < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= Study < 15:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= Study < 16:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= Study < 17:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= Study < 18:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= Study < 19:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= Study < 20:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= Study < 21:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= Study < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= Study < 23:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= Study < 24:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= Study < 25:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= Study < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= Study < 27:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= Study < 28:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= Study < 29:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= Study < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= Study < 31:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= Study < 32:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= Study < 33:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= Study < 34:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= Study < 35:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= Study < 36:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= Study < 37:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= Study < 38:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= Study < 39:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= Study < 40:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= Study < 41:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= Study < 42:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= Study < 43:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= Study < 44:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < Study < 45:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= Study < 46:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= Study < 47:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= Study < 48:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= Study < 49:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= Study < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= Study < 51:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= Study < 52:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= Study < 53:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= Study < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= Study < 55:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= Study < 56:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= Study < 57:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= Study < 58:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= Study < 59:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= Study < 60:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= Study < 61:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= Study < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= Study < 63:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= Study < 64:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= Study < 65:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= Study < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= Study < 67:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= Study < 68:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= Study < 69:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= Study < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= Study < 71:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= Study < 72:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= Study < 73:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= Study < 74:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= Study < 75:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= Study < 76:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 < Study < 77:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= Study < 78:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= Study < 79:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= Study < 80:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= Study < 81:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= Study < 82:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= Study < 83:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= Study < 84:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= Study < 85:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= Study < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= Study < 87:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= Study < 88:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= Study < 89:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= Study < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= Study < 91:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= Study < 92:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= Study < 93:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= Study < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= Study < 95:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= Study < 96:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= Study < 97:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= Study < 98:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= Study < 99:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"

        buttons  = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
          ],
          [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
                


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    Study = math.floor(percentage)
    if 0 < Study <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < Study < 3:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= Study < 4:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= Study < 5:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= Study < 7:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= Study < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= Study < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= Study < 12:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= Study < 13:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < Study < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= Study < 15:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= Study < 16:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= Study < 17:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= Study < 18:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= Study < 19:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= Study < 20:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= Study < 21:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= Study < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= Study < 23:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= Study < 24:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= Study < 25:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= Study < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= Study < 27:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= Study < 28:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= Study < 29:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= Study < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= Study < 31:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= Study < 32:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= Study < 33:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= Study < 34:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= Study < 35:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= Study < 36:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= Study < 37:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= Study < 38:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= Study < 39:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= Study < 40:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= Study < 41:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= Study < 42:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= Study < 43:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= Study < 44:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < Study < 45:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= Study < 46:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= Study < 47:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= Study < 48:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= Study < 49:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= Study < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= Study < 51:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= Study < 52:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= Study < 53:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= Study < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= Study < 55:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= Study < 56:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= Study < 57:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= Study < 58:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= Study < 59:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= Study < 60:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= Study < 61:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= Study < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= Study < 63:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= Study < 64:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= Study < 65:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= Study < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= Study < 67:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= Study < 68:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= Study < 69:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= Study < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= Study < 71:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= Study < 72:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= Study < 73:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= Study < 74:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= Study < 75:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= Study < 76:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 <= Study < 77:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= Study < 78:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= Study < 79:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= Study < 80:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= Study < 81:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= Study < 82:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= Study < 83:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= Study < 84:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= Study < 85:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= Study < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= Study < 87:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= Study < 88:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= Study < 89:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= Study < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= Study < 91:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= Study < 92:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= Study < 93:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= Study < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= Study < 95:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= Study < 96:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= Study < 97:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= Study < 98:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= Study < 99:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
        
        buttons  = [

        [

            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
    
def stream_markup(_, videoid, chat_id):

    buttons  = [   

            [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons

def telegram_markup(_, chat_id):
    buttons  = [   
        
            [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),
            
            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
    ]

    return buttons
## Search Query Inline

def track_markup(_, videoid, user_id, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
## Live Stream Markup

def livestream_markup(_, videoid, user_id, mode, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_3"],

                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text=_["CLOSEMENU_BUTTON"],

                callback_data=f"forceclose {videoid}|{user_id}",

            ),

        ]

    ]

    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text=_["CLOSE_BUTTON"],

                callback_data=f"forceclose {videoid}|{user_id}",

            ),

        ],

    ]

    return buttons
## Slider Query Markup

def slider_markup(

    _, videoid, user_id, query, query_type, channel, fplay

):

    query = f"{query[:20]}"

    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

          ],
          [
          
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="◁",

                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["CLOSE_BUTTON"],

                callback_data=f"forceclose {query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="▷",

                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",

            ),

        ],

    ]

    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 

            [

                [

                    InlineKeyboardButton(

                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"

                    )

                ]    

            ]

        )

## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [  

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="ᴄʟᴏsᴇ", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
