import aiogram
from aiogram import bot, dispatcher
from bot_loading import dp
from handlers import client



async def on_startup(dp:bot):
    print("Бот online")


client.register_handlers_client(dp)

aiogram.executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
 