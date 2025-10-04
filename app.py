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

# Flask route (Telegram webhook uchun)
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# Render test route
@app.route('/')
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
