import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Token Render dagi Environment ga qo'yiladi
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ismlar lug'ati
ismlar = {
    "ali": "Arabcha ism, 'ulug‘' degani.",
    "dilshod": "Forscha, 'xursand yurak'.",
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! 😊 Men Ismlar lug‘ati botman. Ism yuboring.")

@bot.message_handler(func=lambda m: True)
def ism_manosini_top(message):
    ism = message.text.lower().strip()
    if ism in ismlar:
        bot.reply_to(message, f"{ism.capitalize()} ismining ma’nosi:\n{ismlar[ism]}")
    else:
        bot.reply_to(message, "Kechirasiz, bu ism lug‘atda topilmadi ❌.")

# Telegram shu endpointga xabar yuboradi
@app.route("/webhook/"+TOKEN, methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.data.decode("utf-8"))
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/")
def index():
    return "Bot ishlayapti!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
