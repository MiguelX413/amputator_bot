#!/usr/bin/env python3
import logging
import os

from telegram import Update
from telegram.constants import MessageEntityType
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def bot(
    token: str,
) -> None:
    application = ApplicationBuilder().token(token).build()

    echo_handler = MessageHandler(
        filters.TEXT & filters.Entity(MessageEntityType.URL), echo
    )

    application.add_handler(echo_handler)

    application.add_handler(CommandHandler("start", start))

    application.run_polling()


def main() -> None:
    token = os.getenv("token")
    if not isinstance(token, str):
        raise TypeError("No Token")
    logging.basicConfig(level=logging.INFO)
    bot(token)


if __name__ == "__main__":
    main()
