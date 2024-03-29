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


def deamp_url(url: str) -> str:
    # TODO: Use Amputator Bot API
    return url


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "\n".join(
            f"*{deamp_url(url)}"
            for url in update.message.parse_entities(
                types=[MessageEntityType.URL]
            ).values()
        )
    )


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
