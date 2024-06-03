import sqlite3 as sq
import telebot
from my_token import TOKEN


bot = telebot.TeleBot(TOKEN)

def new_users(message): #Перевірка нового користувача

    with sq.connect("DATAFUCK/users.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        # result = cur.fetchall()
        # print(result)
        
        for result in cur:
            if result[0] == message.chat.id:
                exist = True
                break
            else:
                exist = False
        
        if exist != True:
            cur.execute(f'INSERT INTO users(user_id) VALUES({message.chat.id})')
            return True
        else:
            return False

# оновлення стану аудіо (true false)
def turn_audio_false(callback):
    with sq.connect('DATAFUCK/users.db') as con:
        cur = con.cursor()
        cur.execute(f'UPDATE users SET audio = 0 WHERE user_id = {callback.message.chat.id}')
    
def turn_audio_true(callback):
    with sq.connect("DATAFUCK/users.db") as con:
        cur = con.cursor()
        cur.execute(f'UPDATE users SET audio = 1 WHERE user_id = {callback.message.chat.id}')

def check_audio(message):
    with sq.connect("madeinchine/DATAFUCK/users.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        for result in cur:
            if result[0] == message.chat.id:
                return result[1]
            else: continue


def increment_message(message):
    with sq.connect("DATAFUCK/users.db") as con:
        cur = con.cursor()
        cur.execute(f'UPDATE users SET messages = messages + 1 WHERE user_id = {message.chat.id}')


def give_info():
    with sq.connect("DATAFUCK/users.db") as con:
        cur = con.cursor()
        cur.execute(f'SELECT * FROM users')
        result = cur.fetchall()
        title = f'user_id \taudio \tmessage'
        main = ''
        for i in range(0, len(result)):
                # for j in result[i]:
                #         print()
            
            main += f'\n{result[i][0]}    {result[i][1]}    {result[i][2]}'
        text = title + main
    return text
