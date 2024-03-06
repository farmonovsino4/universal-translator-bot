from aiogram import Bot, Dispatcher, executor, types
import logging
import os
from googletrans import Translator
from deep_translator import GoogleTranslator
import pytesseract
from PIL import Image
from gtts import gTTS
from environs import Env

translator = Translator()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
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
        voice =gTTS(text=translated_ru, lang='ru').save('voice.mp3')
        await message.answer(translated_uz)
        await message.answer(translated_ru)
        await message.answer_voice(open('voice.mp3', 'rb'))
    elif lang == 'uz':
        translated_en = GoogleTranslator(source='uz', target='en').translate(message.text)
        translated_ru = GoogleTranslator(source='uz', target='ru').translate(message.text)
        await message.answer(translated_en)
        voice = gTTS(text=translated_en, lang='en').save('voice.mp3')
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
    os.remove("voice.mp3")

@dp.message_handler(content_types=['photo'])
async def image_to_string(message: types.Message):
    await message.answer("qabul qilindi")
    photo = message.photo[-1].file_id
    file_path = await bot.get_file(photo)
    image_bytes = await file_path.download()
    img = Image.open("photos/file_1.jpg")
    text = pytesseract.image_to_string(img)
    lang = translator.detect(text).lang
    if lang == 'en':
        translated_uz = GoogleTranslator(source='en', target='uz').translate(text[:5000])
        translated_ru = GoogleTranslator(source='en', target='ru').translate(text[:5000])
        voice =gTTS(text=translated_ru, lang='ru').save('voice.mp3')
        await message.answer(translated_uz)
        await message.answer(translated_ru)
        await message.answer_voice(open('voice.mp3', 'rb'))
    elif lang == 'uz':
        translated_en = GoogleTranslator(source='uz', target='en').translate(text[:5000])
        translated_ru = GoogleTranslator(source='uz', target='ru').translate(text[:5000])
        await message.answer(translated_en)
        voice = gTTS(text=translated_en, lang='en').save('voice.mp3')
        await message.answer_voice(open('voice.mp3', 'rb'))
        await message.answer(translated_ru)
        voice = gTTS(text=translated_ru, lang='ru').save('voice.mp3')
        await message.answer_voice(open('voice.mp3', 'rb'))
    elif lang == 'ru':
        translated_en = GoogleTranslator(source='ru', target='en').translate(text[:5000])
        translated_uz = GoogleTranslator(source='ru', target='uz').translate(text[:5000])
        await message.answer(translated_en)
        voice = gTTS(text=translated_en, lang='ru').save('voice.mp3')
        await message.answer_voice(open('voice.mp3', 'rb'))
        await message.answer(translated_uz)
    os.remove("voice.mp3")
    img.close()
    # opened = open('photos/file_1.jpg', 'wb')
    # os.remove(str(opened))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)