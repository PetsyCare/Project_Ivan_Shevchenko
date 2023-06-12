#ДЗ на понедельник (отправляем работу скринами - клавиша prtSc, либо скачиваем программу lightshot):
import telebot
from telebot import types
import requests
TOKEN = '5954290853:AAGuDIgoOuSIVSajNNJsZuL8cCzck-Zf_jQ' # SHEVCHENKO_IVAN_BOT
WEATHER_API_key = '886705b4c1182eb1c69f28eb8c520e20'

city = 'Lida'
bot = telebot.TeleBot(TOKEN) #объявляю указатель на телебота

#Добавляем функционал:
#Кнопки:
# 1. Хочу анекдот
# 2. Хочу спать
# 3. Прогноз погоды
def create_keyboard(): # Виртуальная клавиатура
    keyboard = types.InlineKeyboardMarkup() # Создаем клавиатуру
    # Создаем 3 кнопки
    joke_button = types.InlineKeyboardButton(text='😂 Хочу анекдот!',callback_data='1')
    sleep_button = types.InlineKeyboardButton(text='😔 Хочу спать!',callback_data='2')
    weather_button = types.InlineKeyboardButton(text='🌅 Погода!', callback_data='3')
    # Добавили кнопки на кливиатуру
    keyboard.add(joke_button, sleep_button, weather_button)
    return keyboard


# 3. Приветствие
@bot.message_handler(commands=['start'])
def start_bot(message):#функция для приветствия и запуска клавиатуры
    bot.send_message(message.chat.id,'Привет {0.first_name}! \nВас приветствует SHEVCHENK0_IVAN_BOT! \nВыберите, что вы хотите: '.format(message.from_user),reply_markup=create_keyboard())

@bot.callback_query_handler(func= lambda call: True if call.message else False) #этот декоратор перехватывает все calldata
#анонимная функция lambda нужно для того, чтобы отсеить ненужные запросы
# :True означает, что фильтрации не будет и всегда будет True, то есть декоратор сработает при любом запросе (calldata)
def callback_inline(call):
        if call.data == '1':
            res = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1")
            bot.send_message(call.message.chat.id, res.text, reply_markup=create_keyboard())
        if call.data == '2':
            bot.send_message(call.message.chat.id, 'Спокойной ночи!')
        if call.data == '3':
            bot.send_message(call.message.chat.id, 'Введите название города на английском!')
            @bot.message_handler(func=lambda message: True)
            def get_city(message):
                city = message.text
                res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_key}")
                weather_data = res.json()
                bot.send_message(call.message.chat.id, f"Погода в городе {city}:\n\n"
                                                        f"Температура: {weather_data['main']['temp']}°C\n"
                                                        f"Влажность: {weather_data['main']['humidity']}%\n"
                                                        f"Скорость ветра: {weather_data['wind']['speed']} м/с\n", reply_markup=create_keyboard())

bot.polling(none_stop=True)