from aiogram import Bot, Dispatcher, executor, types
import logging
import os
from dotenv import load_dotenv
from googletrans import Translator
from deep_translator import GoogleTranslator
import pytesseract

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Salom <b>{message.from_user.full_name}</b>\nmen universal tarjimon botman", parse_mode='html')

@dp.message_handler()
async def message(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)