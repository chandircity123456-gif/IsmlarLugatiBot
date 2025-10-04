from flask import Flask, request
import telebot

# Bot tokeningizni shu yerga yozasiz
API_TOKEN = "8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE"

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Telegram webhook uchun route
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Oddiy test uchun route
@app.route("/")
def index():
    return "Bot is running!", 200

# Command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men ishlayapman 🚀")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yubordingiz: {message.text}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
