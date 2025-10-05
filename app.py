import telebot
from telebot import types
from flask import Flask, request
import os

API_TOKEN = '8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# === Ismlar lug‘ati ===
ismlar = {
    "ali": "Yuksak, ulug‘, oliy",
    "umar": "Uzoq umrli, yashovchan",
    "hasan": "Chiroyli, go‘zal",
    "husan": "Go‘zal, chiroyli yigit"
}

# === Foydalanuvchidan so‘z olish ===
@bot.message_handler(func=lambda message: True)
def ism_manosi(message):
    ism = message.text.lower().strip()
    if ism in ismlar:
        bot.reply_to(message, f"{ism.capitalize()} ismining ma’nosi:\n{ismlar[ism]}")
    else:
        bot.reply_to(message, "Kechirasiz, bu ism lug‘atda topilmadi ❌")

# === Telegram Webhookdan so‘rov qabul qilish ===
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    try:
        json_str = request.stream.read().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    except Exception as e:
        print("Xatolik:", e)
    return "OK", 200

# === Render health-check ===
@app.route('/')
def index():
    return "Bot is running!", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
