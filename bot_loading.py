import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = aiogram.Bot(token='5013045206:AAHYdwRzv2AmWNXNb_sRBABeS6aQlDRgyn4')
dp = aiogram.Dispatcher(bot, storage=storage)