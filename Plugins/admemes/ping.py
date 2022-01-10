"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "Yah, I'm Currently Alive and All Depends on All MIGHTY"
HELP = "“If you trust in Allah and make Him your companion then all your paths will become easy and safe.”~Ibnul Arabi"
REPO = "“ Only those who can dream big can walk forward in the road of victory.” Ertugrul Bey."
GAME = "𝗚𝗮𝗺𝗲𝘀:- <a href='https://prizes.gamee.com/game-bot/bj6dEMMXfq-d8ee710122e6bea315f3e5849b65026fa59df006#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DkseOJRZzzmGGGzNxgmHQ'>Penalty Shooter</a>, <a href='https://prihttps://prizes.gamee.com/game-bot/a3pyHGoadz-8640829b0401560739b363b29587184489d4e426#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DYXVHJBoOMptiZMaocNyo'>Keep it Up</a>, <a href='https://prizes.gamee.com/game-bot/Q8PWil-57a6b052d76a64ca5037a510f4e3f407fd815286#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DwswnaCYYljtKDFUvyOcU'>F1 Racer</a>, <a href='https://prizes.gamee.com/game-bot/OsqXRuoNE-8bcd07ffa7a8769391452b7e01219953d9ba1059#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DjdnHpqtDIFEpBZbBpVXY'>Skoda Hockey</a>, <a href='https://prizes.gamee.com/game-bot/pocketworldcup-eeb6b9a5fab64233cd46cb900b83e7c41e2205df#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DqHeIGeRrXUXBdmIszbRe'>Pocket World Cup</a>, <a href='https://prizes.gamee.com/game-bot/getaway-fa4dbb4a39edc08fda38ea3291cfb8b21311ee4c#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DRZEEHCHjjnfXhcDHzQRG'>Getaway</a>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
    

@Client.on_message(filters.command("game", COMMAND_HAND_LER) & f_onw_fliter)
async def game(_, message):
    await message.reply_text(GAME)
