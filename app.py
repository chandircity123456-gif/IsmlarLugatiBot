import telebot

TOKEN = "8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE"  # bu joyni keyin almashtiramiz
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! 😊 Men Ismlar lug‘ati botman.")

bot.polling()
