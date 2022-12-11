from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from controller import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    # await update.message.reply_text(update.message.text)
    result = calculator(update.message.text)
    await update.message.reply_text(f"Результат вычисления равен {result}")


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Введите рациональное выражения для расчета: ")
    # await update.message.reply_text(f"Вы ввели строчку {update.message.text[6:]}")
    #


def main() -> None:
    """Start the bot."""
    with open('token.txt', mode='r') as data:
        my_token = data.readline()

    application = Application.builder().token(my_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calc", calc))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()




# В консоле window активация виртуального окружения выполняется .\activate в папки где расположен данный файл(в данном случае папка venv\script)
# В консоле window деактивация виртуального окружения выполняется .\deactivate в папки где расположен данный файл(в данном случае папка venv\script)
# запуск бота выполняется командой python main.py

# pip install python-telegram-bot --pre