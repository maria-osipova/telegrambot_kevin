import telebot
from telebot import types

bot = telebot.TeleBot('6774068511:AAFLW29l_cz1slADWNIp1ud8C1WbYaFsRpwI')

# Dictionary to store the user's messages
user_responses = {}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('да', callback_data='yes'
    btn2 = types.InlineKeyboardButton('нет', callback_data='no')
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name}! придет ли сегодня Кевин?', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    user_name =  callback.from_user.first_name
    choice = callback.data

    if callback.data == 'yes':
        user_responses[user_id] = 'окей! спасибо, что предупредил!'
        bot.send_message('635793659', 'купи сендвичи')
    elif callback.data == 'no':
        user_responses[user_id] = 'окей, спасибо, что предупредил.'
        bot.send_message('635793659', 'не покупай')

    # Edit the original message to include the user's response
    if user_id in user_responses:
        bot.edit_message_text(user_responses[user_id], chat_id, callback.message.message_id)
        bot.delete_message(chat_id, callback.message.message_id - 1)

bot.polling(non_stop=True)

