from bot import bot, dp

from aiogram.types import Message
from config import admin_id, admin_id2

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot had started!")
    await bot.send_message(chat_id=admin_id2, text="Bot had started!")