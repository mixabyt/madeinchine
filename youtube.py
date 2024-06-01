import telebot
from pytube import YouTube
import os
import random

from my_token import TOKEN
from DATAFUCK.act_with_data import check_audio

bot = telebot.TeleBot(TOKEN)




def correct_name(name):
    ban_symbols = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']

    correct = name
    for symbol in ban_symbols:
        if symbol in name:
            correct = name.replace(symbol, '')
    return correct



def delete_video(name):
    file_path = f'{name}.mp4'
    try:
        os.remove(file_path)
    except:
        print('не знайдено файл')


def delete_audio(name):
    file_path = f'{name}.mp3'
    try:
        os.remove(file_path)
    except:
        print('не знайдено файл')


def send_youtube_video(message):
    try:
        yt = YouTube(message.text)
        chosen_stream = yt.streams.get_highest_resolution()

        if yt.streams.get_highest_resolution().filesize > 100000000:

            bot.send_message(message.chat.id, f'файл превищує 50мб')
            return False
        else:

            number_name = random.randint(1, 1000000000)
            chosen_stream.download(filename = f'{number_name}.mp4')

            video = open(f'{number_name}.mp4', 'rb')
            bot.send_video(message.chat.id, video)


            video.close()
            delete_video(number_name)


    except:
        bot.send_message(message.chat.id, 'щось пішло не так...')
        return False


def send_youtube_audio(message):
    if check_audio(message) == False:
        pass
    else:
        try:
            yt = YouTube(message.text)

            name = yt.title
            name = correct_name(name)
            
            chosen_stream = yt.streams[-1]
            chosen_stream.download(filename=f'{name}.mp3')

            audio = open(f'{name}.mp3', 'rb')

            bot.send_audio(message.chat.id, audio, title=name[:], performer='madeinchinebot')

            audio.close()
            delete_audio(name)


        except:
            bot.send_message(message.chat.id, "fuck fuck")

                                                            

                                                    
