from pyrogram import filters
from pyrogram.types import Message

from Romeo.utilities.config import BANNED_USERS
from Romeo.utilities.strings import get_command
from Romeo.utilities.events.command import command
from Romeo import bot
from Romeo.modules.core.call import main
from Romeo.modules.database import is_music_playing, music_off
from Romeo.modules.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@bot.on_message(
    command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await main.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )
