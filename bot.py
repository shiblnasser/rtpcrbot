import telebot
import time

TOKEN = "2141606527:AAE68W8Srub0KrRfdDqhjap4po_2HAo7_TI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["hello"])
def greet(message):
    bot.reply_to(message = message , text = "asdasd")



bot.polling()