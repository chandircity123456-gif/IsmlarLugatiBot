import os
from flask import Flask, request
import telebot

# Tokenni Render environment variables ichidan olish
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Ismlar lug‘ati
ismlar = {
    "ali": "Arabcha ism, 'ulug‘' degani.",
    "dilshod": "Forscha, 'xursand yurak'.",
    "umid": "Arabcha, 'ishonch', 'umid'.",
    "madina": "Arabcha, 'shahar', 'go‘zal joy'."
}

# Start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot
