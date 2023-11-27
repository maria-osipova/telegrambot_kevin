import telebot
from telebot import types
#from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

bot = telebot.TeleBot('6774068511:AAFLW29l_cz1slADWNIp1u8C1WbYaFsRpwI')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('да', callback_data='yes')
    btn2 = types.InlineKeyboardButton('нет', callback_data='no')
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name}! придет ли сегодня Кевин?', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'yes':
        bot.send_message(callback.message.chat.id, 'ок, спасибо, что предупредил')
    elif callback.data == 'no':
        bot.send_message(callback.message.chat.id, 'ок, спасибо, что предупредил')

bot.polling(non_stop=True)

