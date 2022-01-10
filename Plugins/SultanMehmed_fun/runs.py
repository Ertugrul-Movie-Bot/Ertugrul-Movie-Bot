import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
"<a href='https://telegra.ph/file/6ce10f7c7d81d6fb9d091.jpg'>❤️</a>“The seed which is not willing to let its shell rot, can not bear fruits.” Ertugrul Bey",
"<a href='https://telegra.ph/file/82704920aec486551e021.jpg'>❤️</a>“I am only the enemy of oppression and betrayal.” Ertugrul Bey",
"<a href='https://telegra.ph/file/a64458a391dd22b326346.jpg'>❤️</a>“Patience is bitter, but its fruit is sweet.” Turgut Alp",
)


@Client.on_message(
    filters.command("qoute", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def qoute(_, message):
    """ /qoute strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
