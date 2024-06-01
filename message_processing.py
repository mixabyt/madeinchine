import telebot
from telebot import types

from my_token import TOKEN

from DATAFUCK.act_with_data import turn_audio_true, turn_audio_false
from DATAFUCK.act_with_data import check_audio
bot = telebot.TeleBot(TOKEN)

def youtube_link(message):
    return "youtube.com" in message.text or 'youtu.be' in message.text

def tiktok_link(message):
    return 'tiktok.com' in message.text

def press_button(message):
    if check_audio (message) == True:
        kb = types.InlineKeyboardMarkup(row_width=1)
        audio = types.InlineKeyboardButton(text="Надсилати аудіо ✅ ", callback_data="audio-")
        kb.add(audio)
        bot.send_message(message.chat.id, text="Налаштуванння чату:", reply_markup=kb)
    else:
        kb = types.InlineKeyboardMarkup(row_width=1)
        audio = types.InlineKeyboardButton(text="Надсилати аудіо ❌ ", callback_data="audio+")
        kb.add(audio)
        bot.send_message(message.chat.id, text="Налаштуванння чату:", reply_markup=kb)


def turn_audio(callback):
    if callback.data == 'audio-':
        kb = types.InlineKeyboardMarkup(row_width=1)
        audio = types.InlineKeyboardButton(text="Надсилати аудіо ❌ ", callback_data="audio+")
        kb.add(audio)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Налаштуванння чату:", reply_markup=kb)
        turn_audio_false(callback)


    if callback.data == 'audio+':
        kb = types.InlineKeyboardMarkup(row_width=1)
        audio = types.InlineKeyboardButton(text="Надсилати аудіо ✅ ", callback_data="audio-")
        kb.add(audio)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Налаштуванння чату:", reply_markup=kb)
        turn_audio_true(callback)
