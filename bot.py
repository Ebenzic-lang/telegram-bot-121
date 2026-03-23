import telebot
import os

TOKEN = os.getenv("8734287473:AAEk5NC2uxMiV_Ne13qf-Q9s244cJyPFPx8")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is live 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
