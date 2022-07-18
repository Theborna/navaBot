import os
from requests import request
import requests
import telebot

API_KEY = "5574991692:AAF9OchV350KsuPne9S5PrGr3G2W-1yZf9k"

bot = telebot.TeleBot(API_KEY)


def hasKos(message):
    request = message.text
    validKos = ["کث", "کص", "کوبص", "کوبث", "کوص", "کوث"]
    for kos in validKos:
        if kos in request:
            return True
    return False


@bot.message_handler(commands=["Greet"])
def greet(message):
    bot.reply_to(message, "kos mikham")


@bot.message_handler(func=hasKos)
def correctKos(message):
    bot.reply_to(message, "س")


bot.polling()