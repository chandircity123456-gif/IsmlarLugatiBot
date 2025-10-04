import os
from flask import Flask, request
import telebot

# Render Environment Variables dan token olish
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Ismlar lug‘ati
ismlar = {
    "ali": "Arabcha ism, 'ulug‘' degani.",
    "dilshod": "Forscha, 'xursand yurak'.",
}

# Start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! 😊 Men Ismlar lug‘ati botman. Ism yuboring.")

# Ism ma’nosini topish
@bot.message_handler(func=lambda m: True)
def ism_manosini_top(message):
    ism = message.text.lower().strip()
    if ism in ismlar:
        bot.reply_to(message, f"{ism.capitalize()} ismining ma’nosi:\n{ismlar[ism]}")
    else:
        bot.reply_to(message, "Kechirasiz, bu ism lug‘atda topilmadi ❌.")

# Flask route (Render uchun)
@app.route('/')
def index():
    return "Bot is running!"

# Telegram webhook yoki polling ishga tushirish
if __name__ == "__main__":
    bot.polling(none_stop=True)
