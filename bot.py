from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def mulai(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Selamat datang, {update.effective_user.first_name}! Saya adalah bot Telegram Anda.")

async def tolong(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Saya dapat membantu Anda! Ketik pesan apa saja untuk mencoba.")
    
async def puisi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("senyuman mu bagai mawar, indah setiap hari, dan cantikmu kaya matahari bersinar setiap aku melihatmu")
    
async def pantun(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Makan es krim sambil duduk santai,Tiba-tiba hati jadi melayang. Kau senyum padaku, aku jadi baper,Hati ini pun terhanyut dalam bayang.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    await update.message.reply_text(f" {user_message}")

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN tidak ditemukan. Pastikan Anda telah mengatur file .env dengan benar.")
        return

    
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", mulai))
    application.add_handler(CommandHandler("help", tolong))
    application.add_handler(CommandHandler("puisi", puisi))
    application.add_handler(CommandHandler("pantun", pantun))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    application.run_polling()

if __name__ == "__main__":
    main()

