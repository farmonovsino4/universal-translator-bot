from aiogram import Bot, Dispatcher, executor, types
import logging
import os
from dotenv import load_dotenv
from googletrans import Translator
from deep_translator import GoogleTranslator
import pytesseract
from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Salom <b>{message.from_user.full_name}</b>\nmen universal tarjimon botman", parse_mode='html')

@dp.message_handler()
async def message(message: types.Message):
    lang = translator.detect(message.text).lang
    if lang == 'en':
        translated_uz = GoogleTranslator(source='en', target='uz').translate(message.text)
        translated_ru = GoogleTranslator(source='en', target='ru').translate(message.text)
        voice =gTTS(text=translated_uz, lang='ru').save('voice.mp3')
        await message.answer(translated_uz)
        await message.answer(translated_ru)
        await message.answer_voice(open('voice.mp3', 'rb'))
    elif lang == 'uz':
        translated_en = GoogleTranslator(source='uz', target='en').translate(message.text)
        translated_ru = GoogleTranslator(source='uz', target='ru').translate(message.text)
        await message.answer(translated_en)
        voice = gTTS(text=translated_en, lang='ru').save('voice.mp3')
        await message.answer_voice(open('voice.mp3', 'rb'))
        await message.answer(translated_ru)
        voice = gTTS(text=translated_ru, lang='ru').save('voice.mp3')
        await message.answer_voice(open('voice.mp3', 'rb'))
    elif lang == 'ru':
        translated_en = GoogleTranslator(source='ru', target='en').translate(message.text)
        translated_uz = GoogleTranslator(source='ru', target='uz').translate(message.text)
        await message.answer(translated_en)
        voice = gTTS(text=translated_en, lang='ru').save('voice.mp3')
        await message.answer_voice(open('voice.mp3', 'rb'))
        await message.answer(translated_uz)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)