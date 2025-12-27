from config import token
from main import Car
import telebot
import random
import telebot.util

bot = telebot.TeleBot(token)

quotes = [
    "Сделай первый шаг, и ты поймешь, что не все так страшно. — Сенека",
    "Лучший способ предсказать будущее — создать его. — Авраам Линкольн",
    "Мы — это то, что мы делаем постоянно. — Аристотель",
    "Жизнь — это то, что происходит с нами, пока мы строим другие планы. — Джон Леннон"
]

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['car'])
def create_car(message):
    args_text = telebot.util.extract_arguments(message.text)
    
    if not args_text:
        car = Car()
        bot.reply_to(message, "Ваш автомобиль\n" + car.info())
        return
    
    args = args_text.split()
    
    if len(args) == 1:
        car = Car(color=args[0])
    elif len(args) == 2:
        car = Car(color=args[0], car_brand=args[1])
    elif len(args) >= 3:
        car = Car(color=args[0], car_brand=args[1], year=args[2])
    else:
        car = Car()
    
    bot.reply_to(message, "Создан автомобиль:\n" + car.info())

@bot.message_handler(commands=['quote'])
def quote_handler(message):
    quote = random.choice(quotes)
    bot.reply_to(message, quote)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
