import telebot
from time import sleep

from my_token import TOKEN
from youtube import send_youtube_video
from youtube import send_youtube_audio
from DATAFUCK.act_with_data import new_users
from message_processing import *
from tiktok import send_tiktok_video, send_tiktok_audio
from DATAFUCK.act_with_data import increment_message, give_info

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def get_start(message):
    new_users(message)
    bot.send_message(message.chat.id, f'Привіт!\n\
Щоб завантажити відео або звук з YouTube або TikTok — надішли мені посилання.')
    increment_message(message)
    


@bot.message_handler(commands=['settings'])
def settings(message):
    press_button(message)
    increment_message(message)
    

@bot.message_handler(commands=['info'])
def info_database(message):
    if message.chat.id == 713774587:
        bot.send_message(message.chat.id, give_info())        



# @bot.message_handler(content_types=['video'])
# def video_editor(message):
#     video = message.video.file_id
#     # bot.send_video_note(message.chat.id, video)
#     file_info = bot.get_file(video)
#     video_path = file_info.file_path
#     video_clip = VideoFileClip(video_path)
#     video_note_path = "D:\\tbot\\"
#     video_clip.write_videofile(video_note_path, audio=False, codec="libx264", fps=24)

#     bot.send_video_note(message.chat.id , open(video_note_path, 'rb'))

#     video_clip.close()
#     os.remove(video_note_path)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    turn_audio(callback)
    
 

@bot.message_handler(func=youtube_link)
def link(message):
    if send_youtube_video(message) != False:
        send_youtube_audio(message)
    increment_message(message)

    
@bot.message_handler(func=tiktok_link)
def start_fuck(message):
    if send_tiktok_video(message) != False:
        send_tiktok_audio(message)
    increment_message(message)



@bot.message_handler(func= lambda message: True)
def other(message):
    increment_message(message)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)
