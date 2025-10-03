import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters, CommandHandler
from ismlar import ISMLAR_LUGATI 

# !!! TOKENINGIZ RENDER MUAMMOLARI TUFAYLI BU YERGA QO'YILGAN !!!
TOKEN = "8422115593:AAH_9RJtYUSp8IyDfdt9qbKsDoaC0tSjuZE" 
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", None)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # "lug'ati" so'zidagi yakka tirnoq (\') bilan almashtirildi
    xabar = "Assalomu alaykum! Ismlar lug'ati botiga xush kelibsiz.\n"
    xabar += "Menga ma'nosini bilmoqchi bo'lgan **ismni yuboring**."
    await update.message.reply_text(xabar)

async def ism_qidirish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    qidiriladigan_ism = update.message.text
    kalit_soz = qidiriladigan_ism.lower().strip()
    
    if kalit_soz in ISMLAR_LUGATI:
        ma'nosi = ISMLAR_LUGATI[kalit_soz]
        # "ma'nosi" so'zidagi yakka tirnoq (\') bilan almashtirildi
        javob = f"**{qidiriladigan_ism.capitalize()}** ismining ma\'nosi:\n\n_{ma\'nosi}_" 
    else:
        # "Kechirasiz" va "ma'nosi" so'zidagi yakka tirnoq (\') bilan almashtirildi
        javob = f"Kechirasiz, **{qidiriladigan_ism.capitalize()}** ismining ma\'nosi lug\'atda topilmadi."

    await update.message.reply_text(javob, parse_mode='Markdown')

def main() -> None:
    port = int(os.environ.get("PORT", 8080))
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ism_qidirish))
        
    if WEBHOOK_URL:
        print(f"Webhook rejimida {port} portida ishga tushirilmoqda...")
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=WEBHOOK_URL + '/' + TOKEN
        )
    else:
        print("WEBHOOK_URL topilmadi. Polling rejimida ishga tushirilmoqda.")
        app.run_polling()


if __name__ == "__main__":
    main()
