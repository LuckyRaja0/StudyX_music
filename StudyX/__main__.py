import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from StudyX import LOGGER, app, userbot
from StudyX.core.call import Study
from StudyX.plugins import ALL_MODULES
from StudyX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("StudyX").error(
            "BETA KM SE KM EK ID TO ASSISTANT KE LIYE DE CHUP CHAP EK PAROGRAM SESSION BNA KE DAL..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("StudyX").warning(
            "DEKH HME NA BOLIYO KI SPORTIFY SE GANE NA CHEL RE KYUKI USKA ID OR SECRET DAL TAB CHLEGA."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("StudyX.plugins." + all_module)
    LOGGER("StudyX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Study.start()
    try:
        await Study.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Study.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("StudyX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Study.decorators()
    LOGGER("StudyX").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 ����𝘆 ��𝗝�♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("StudyX").info("Stopping Music Bot...")
