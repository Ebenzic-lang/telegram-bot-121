import telebot
import os

# Get token from Render environment
TOKEN = os.environ.get("8734287473:AAEupAPw0jrZiLMZlqwCCwcWzznG-srqYkw")

# Safety check (prevents crash like before)
if not TOKEN:
    raise ValueError("No BOT_TOKEN found. Please add it in Render Environment Variables.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is live and working!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

print("🤖 Bot is running...")
bot.infinity_polling()
