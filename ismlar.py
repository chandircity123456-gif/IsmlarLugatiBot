import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters, CommandHandler
from ismlar import ISMLAR_LUGATI 

# !!! BOT TOKENINGIZ O'RNATILGAN !!!
# Renderda bu o'zgaruvchi Environment Variable orqali o'qilishi kerak
TOKEN = "8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE" 
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", None)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Apostrof (`) xatolarini hal qilish uchun uch qo'sh tirnoq (""") ishlatildi.
    xabar = """Assalomu alaykum! Ismlar lug'ati botiga xush kelibsiz.
Menga ma'nosini bilmoqchi bo'lgan **ismni yuboring**."""
    await update.message.reply_text(xabar, parse_mode='Markdown')

async def ism_qidirish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    qidiriladigan_ism = update.message.text
    # Lug'at kalitlariga moslash uchun matnni tozalaymiz
    kalit_soz = qidiriladigan_ism.lower().strip()
    
    if kalit_soz in ISMLAR_LUGATI:
        ma'nosi = ISMLAR_LUGATI[kalit_soz]
        # Xatoga sabab bo'luvchi barcha apostroflar uch tirnoq ichiga olindi.
        javob = f"""**{qidiriladigan_ism.capitalize()}** ismining ma'nosi:

_{ma'nosi}_""" 
    else:
        # Boshqa xato chiqmasligi uchun qattiq tekshirildi.
        javob = f"""Kechirasiz, **{qidiriladigan_ism.capitalize()}** ismining ma'nosi lug'atda topilmadi."""

    await update.message.reply_text(javob, parse_mode='Markdown')

def main() -> None:
    # Render avtomatik ravishda PORT ni o'rnatadi.
    port = int(os.environ.get("PORT", 8080))
    app = Application.builder().token(TOKEN).build()
    
    # Buyruqlarni boshqarish
    app.add_handler(CommandHandler("start", start_command))
    # Matnli xabarlarni boshqarish
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ism_qidirish))
        
    if WEBHOOK_URL:
        # Renderda ishlatish uchun Webhook rejimini ishga tushirish
        print(f"Webhook rejimida {port} portida ishga tushirilmoqda...")
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=WEBHOOK_URL + '/' + TOKEN
        )
    else:
        # Mahalli kompyuterda ishlatish uchun Polling rejimini ishga tushirish
        print("WEBHOOK_URL topilmadi. Polling rejimida ishga tushirilmoqda.")
        app.run_polling()


if __name__ == "__main__":
    main()
