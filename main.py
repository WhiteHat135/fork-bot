""" Import Module """
import telebot
""" Main vars """
chat_id = "-1001461305516"
""" Profile"""
bot = telebot.TeleBot("869011883:AAFkJ1IEfaqf9bD5RxGekz9L2Xf7z0JCECo")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat_id, "Привет, я Меттатон бот. Давай знакомиться!")
bot.polling()
