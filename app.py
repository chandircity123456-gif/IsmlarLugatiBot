import os
import telebot
from flask import Flask, request

# 🔑 Telegram BOT Token
API_TOKEN = "8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE"

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 🟢 Misol uchun oddiy ism lug‘ati
ismlar = {
    "ali": "Yuqori martabali, sharafli.",
    "vali": "Do‘st, yordamchi.",
    "jasur": "Qo‘rqmas, botir."
}

# 🔹 Foydalanuvchi xabar yuborganda javob
@bot.message_handler(func=lambda message: True)
def ism_manosini_top(message):
    ism = message.text.lower().strip()
    if ism in ismlar:
        bot.reply_to(message, f"{ism.capitalize()} ismining ma’nosi:\n{ismlar[ism]}")
    else:
        bot.reply_to(message, "Kechirasiz, bu ism lug‘atda topilmadi ❌.")

# 🔹 Telegram webhook POST endpoint
@app.route("/" + API_TOKEN, methods=['POST'])
def getMessage():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# 🔹 Render health check (tekshirish uchun)
@app.route("/", methods=['GET'])
def index():
    return "Bot is running!", 200

# 🔹 Localda ishlatish uchun
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
