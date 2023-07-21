import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
from db_functions import useridea


logging.basicConfig(level=logging.INFO)

API_TOKEN='6210304664:AAEFyc4k6hn3y-9TDNFXapwWPzf4LMSlxa4'
# API_TOKEN = os.environ.get('API_TOKEN', '')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.reply("Привет! Введите свою идею.")


@dp.message_handler(content_types=types.ContentType.TEXT)
async def on_text(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_idea = message.text

    useridea(user_idea, user_name, user_id)

    await message.reply("Спасибо! Я сохранил ее в бд. Какая следующая идея?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
