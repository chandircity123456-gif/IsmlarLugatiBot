import telebot

# Bu yerga o'zingizning BotFather'dan olgan tokeningizni kiriting
TOKEN = "8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE"

bot = telebot.TeleBot(TOKEN)

# Ismlar lug‘ati (boshlanish uchun bir nechta misollar)
ismlar = {
    "ali": "Arabcha ism, ‘ulug‘’, ‘baland martabali’ degan ma’noni anglatadi.",
    "zulfiya": "Arabcha so‘z bo‘lib, ‘nozik’, ‘muloyim’ degan ma’noni anglatadi.",
    "dilshod": "Forscha so‘z; ‘xursand yurak’ degan ma’noda ishlatiladi.",
    "diyor": "Yurt, mamlakat, o‘lka ma’nosida.",
    "oybek": "Oydek yorug‘ va pok degan ma’noda.",
    "nodira": "Noyob, qimmatli degan ma’noda."
}

# /start buyrug‘i uchun handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! 🙂 Men Ismlar lug‘ati botman.\n"
                          "Ism yuboring, men uning ma’nosini aytaman.")

# Istalgan matn yuborilganda ishlaydi
@bot.message_handler(func=lambda message: True)
def ism_manosini_top(message):
    ism = message.text.lower()
    if ism in ismlar:
        bot.reply_to(message, f"👉 {ism.capitalize()} ismining ma’nosi:\n{ismlar[ism]}")
    else:
        bot.reply_to(message, "Kechirasiz, bu ism lug‘atda topilmadi ❌.\n"
                              "Boshqa ism yuboring.")

print("🤖 Bot ishga tushdi...")
bot.infinity_polling()
