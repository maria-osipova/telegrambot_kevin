import telebot
from telebot import types
import schedule
from time import sleep
from threading import Thread

bot = telebot.TeleBot('6774068511:AAFLW29l_cz1slADWNIp1u8C1WbYaFsRpwI')

user_responses = {}
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_name = message.from_user.first_name

    user_data[user_id] = {'chat_id': user_id, 'user_name': user_name}
    print("Received /start from user:", user_id, "User data:", user_data)

    bot.send_message(user_id, 'Привет!')

def schedule_checker():
    while True:
        schedule.run_pending()

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    user_name = callback.from_user.first_name

    if user_id not in user_data:
        user_data[user_id] = {'chat_id': chat_id, 'user_name': user_name}
        print("New user data added:", user_data)

    if callback.data == 'yes':
        user_responses[user_id] = 'окей! спасибо, что предупредил!'
        bot.send_message('635793659', 'купи сендвичи')
    elif callback.data == 'no':
        user_responses[user_id] = 'окей, спасибо, что предупредил.'
        bot.send_message('635793659', 'не покупай')

    if user_id in user_responses:
        bot.edit_message_text(user_responses[user_id], chat_id, callback.message.message_id)
        bot.delete_message(chat_id, callback.message.message_id - 1)
def function_to_run():
    if not user_data:  # Проверка, что в user_data есть данные
        print("No messages received yet.")
        return

    for user_id, details in user_data.items():
        chat_id = details['chat_id']
        user_name = details['user_name']
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('да', callback_data='yes')
        btn2 = types.InlineKeyboardButton('нет', callback_data='no')
        markup.add(btn1, btn2)

        try:
            bot.send_message(chat_id, f'Привет, {user_name}! Придет ли сегодня Кевин?', reply_markup=markup)
        except Exception as e:
            print(f"Error sending message to {chat_id}: {e}")  # Логирование ошибки

if __name__ == "__main__":
    schedule.every().tuesday.at("14:25").do(function_to_run)
    Thread(target=schedule_checker).start()
    bot.polling(non_stop=True)


