from pyrogram import filters
from pyrogram.types import Message

from Romeo.utilities.config import BANNED_USERS
from Romeo.utilities.strings import get_command
from Romeo import bot
from Romeo.modules.core.call import main
from Romeo.modules.database import is_muted, mute_off
from Romeo.modules.decorators import AdminRightsCheck

# Commands
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")


@bot.on_message(
    filters.command(UNMUTE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"])
    await mute_off(chat_id)
    await main.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention)
    )
