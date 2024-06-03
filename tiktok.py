import telebot
import requests
import os

from DATAFUCK.act_with_data import check_audio
from my_token import TOKEN


bot = telebot.TeleBot(TOKEN)



def delete_tiktok(name):
    file_path = f'{name}'
    try:
        os.remove(file_path)
    except:
        print('error')



def download_tiktok_video(message):
    try:
        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

        querystring = {"url":message.text,"hd":"1"}

        headers = {
            "X-RapidAPI-Key": "YOURKEY",
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }


        response = requests.get(url, headers=headers, params=querystring)

        video_link = response.json()['data']['play']
        video_name = response.json()['data']['music_info']['title']
        response = requests.get(url=video_link)
        with open(f'{video_name}.mp4', 'wb') as file:
              file.write(response.content)
        return video_name
    except Exception as err:
        bot.send_message(713774587, f'{err}')
        return False




def send_tiktok_audio(message, name):
    if check_audio(message) == False:
        return False
    else:
        try:
            audio = open(f'{name}.mp3', 'rb')
            bot.send_audio(message.chat.id, audio, title=f'{name}', performer='madeinchine')
            audio.close()
        except:
            bot.send_message(message.chat.id, f'помилка аудіо')
            return False


def send_tiktok_video(message, name):
    try:
        video = open(f'{name}.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        video.close()
    except: return False



def send_tiktok(message):
    name = download_tiktok_video(message)
    if name == False:
        return
    if send_tiktok_video(message, name) != False:
        os.rename(f'{name}.mp4', f'{name}.mp3')
        send_tiktok_audio(message, name)
        delete_tiktok(f'{name}.mp3')


                                                       

                                           
