""" Import Module """
from telegram.ext import Updater, CommandHandler
import logging
""" Main vars """
chat_id = "-1001461305516"
token = '869011883:AAFkJ1IEfaqf9bD5RxGekz9L2Xf7z0JCECo'

""" Debuging """
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    update.warning.reply_text()

def test(update, context):
    update.message.reply_text("Test")
""" Main """
def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("test", test))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()