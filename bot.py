import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_BOT_TOKEN = 'Key'
OPENAI_API_KEY = 'Key'

openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

async def chat_with_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text("Ocurrió un error 😕")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot conectado a OpenAI 🤖")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gpt))

    app.run_polling()

if __name__ == '__main__':
    main()
