import os

from dotenv import load_dotenv, find_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv(find_dotenv(".env"))


def load_locale_text(language):
    file_path = f"locale/{language}.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().split("\n")


async def language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    language = query.data
    text_lines = load_locale_text(language)

    web_app_url = os.getenv("WEB_APP_URL")
    keyboard = [
        [
            InlineKeyboardButton(
                text=text_lines[-1],
                web_app=WebAppInfo(url=web_app_url)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        text="\n".join(text_lines[:-1]),
        reply_markup=reply_markup
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")],
        [InlineKeyboardButton(text="🇺🇸 English", callback_data="en")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text="Tilni tanlang:\nВыберите язык:\nSelect language:",
        reply_markup=reply_markup
    )


if __name__ == '__main__':
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_selection))

    print("Bot ishga tushdi!")
    app.run_polling()
