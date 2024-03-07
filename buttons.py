from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

voice_btn = InlineKeyboardMarkup().add(
    InlineKeyboardButton("🎤 Voice", callback_data="voice")
)