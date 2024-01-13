import telebot
import requests
import pyktok as pyk
import os
import random

from DATAFUCK.act_with_data import check_audio
from my_token import TOKEN


bot = telebot.TeleBot(TOKEN)


def find_audio(message):
    part_of_name = ''
    if 'ZM' in message.text:
        part_of_name = 'ZM'
    else:    
        for name in message.text[23:]:
            if name == '/':
                break
            else:
                part_of_name += name
    way_to = 'D:\\telebot\\'

    file_in_catalogy = os.listdir(way_to)

    found = [file for file in file_in_catalogy if part_of_name in file]

    num = random.randint(1,30)
    new_name = f'{part_of_name}{num}.mp3'
    os.rename(found[0], new_name)
    return new_name
    


def delete_tiktok_audio(name):
    file_path = f'{name}'
    try:
        os.remove(file_path)
        os.remove("video_data.cvs")
    except:
        print('error')



def send_tiktok_video(message):
    try:
        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

        querystring = {"url":message.text,"hd":"1"}

        headers = {
            "X-RapidAPI-Key": "ec53cc09f6msh39d86230f7f1046p1a67f6jsn09c1d5577c9c",
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }

    
        response = requests.get(url, headers=headers, params=querystring)
        video_link = response.json()['data']['play']
        bot.send_video(message.chat.id, video_link)
    except:
        return False
    
    
    

def send_tiktok_audio(message):
    if check_audio(message) == False:
        pass
    else:
        try:
            pyk.save_tiktok(f'{message.text}', True, 'video_data.cvs', browser_name='chrome')
            
            name = find_audio(message)
            audio = open(name, 'rb')
            
            bot.send_audio(message.chat.id, audio, title=name[:] ,performer='madeinchine')
            
            audio.close()
            delete_tiktok_audio(name)
        except:
            return
    



