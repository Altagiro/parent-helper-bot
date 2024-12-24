import telebot
import config

bot = telebot.TeleBot(config.TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there! This is a simple bot designed to help parents by alerting them about upcoming developmental crises in their child")


bot.infinity_polling()
