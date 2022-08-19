import csv
import os
from email import message

import mysql.connector
import pandas as pd
import telebot
from telebot.types import Message as tg_msg
from attr import has
from dotenv import load_dotenv
from mysql.connector import Error
from requests import request

load_dotenv()
API_KEY = os.getenv('API_KEY')
DEF_STICKER = 'CAACAgIAAxkBAANQYwABAkfaBCofCnm1PiZ33BqNkXWyAAJSFAACmZFpSoLElaTaSqdLKQQ'

bot = telebot.TeleBot(API_KEY)

header = ['chat_id', 'message', 'reply']


def addFilter(chat_id, message, reply):
    with open('filters.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([chat_id, message, reply])

# pw = "kos"


# def create_server_connection(host_name, user_name, user_password):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password
#         )
#         print("MySQL Database connection successful")
#     except Error as err:
#         print(f"Error: '{err}'")

#     return connection


# connection = create_server_connection("localhost", "root", pw)


def hasKos(message: tg_msg):
    request = message.text
    validKos = ["کث", "کص", "کوبص", "کوبث", "کوص", "کوث"]
    for kos in validKos:
        if kos in request:
            return True
    return False


@bot.message_handler(commands=["greet"])
def greet(message: tg_msg):
    bot.reply_to(message, "kos mikham")


@bot.message_handler(func=hasKos)
def correctKos(message: tg_msg):
    bot.reply_to(message, "س")
    bot.send_sticker(chat_id=message.chat.id,
                     sticker=DEF_STICKER)


@bot.message_handler(commands=["Filter"])
def addFilter(message: tg_msg):
    if message.text == "/Filter" or message.text == "/Filter ":
        bot.reply_to(message, "Filter cannot be empty")
        return
    command = message.text.replace("/Filter ", "", 1)
    if message.reply_to_message is None:
        bot.reply_to(message, "Filter cannot be empty")
        return
    print("added filter "+"{command}"+" with " +
          "{message.reply_to_message.text}")
    with open('filters.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([message.chat.id, command,
                        message.reply_to_message.text])


def check_filter(message: tg_msg):
    data = pd.read_csv("filters.csv")
    x = data.chat_id
    print(x)
    return True


# @bot.message_handler(func=check_filter)
# def javab(message : tg_msg):
#     print(message.chat.id)


def isKos(message: tg_msg):
    if message.text == "کس":
        return True
    return False


@bot.message_handler(func=isKos)
def addFilter(message: tg_msg):
    bot.reply_to(message, "میخوام")

bot.polling()
