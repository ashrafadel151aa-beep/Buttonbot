import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 ملخصات")
    btn2 = types.KeyboardButton("📞 تواصل")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "أهلاً بيك! اختار من الأزرار اللي تحت 👇", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "📚 ملخصات":
        bot.send_message(message.chat.id, "هنا هتلاقي كل الملخصات 🧠\nhttps://t.me/yourchannel")
    elif message.text == "📞 تواصل":
        bot.send_message(message.chat.id, "تقدر تبعتلي هنا أي وقت ❤️")
    else:
        bot.send_message(message.chat.id, "اختار من الأزرار اللي تحت يا نجم 😎")

bot.infinity_polling()
