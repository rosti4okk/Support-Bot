import telebot
from telebot import types

TOKEN = '6512193022:AAH_FdiUokc_hdY5TPyu_zr4475KSQ_xccQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='💖 Питання 💖', callback_data = 'btn1')
    btn2 = types.InlineKeyboardButton(text='💁‍♂️ Пропозиція 💁‍♂️', callback_data = 'btn2')
    btn3 = types.InlineKeyboardButton(text='🎧 Запропонувати Пісню 🎧', callback_data = 'btn3')
    kb.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Привіт ❤️!\nЦе бот підтримки телеграм каналу\nᴍᴜsɪᴄ 💞.\nВи можете надіслати нам своє питання або пропозицію і ми обов'язково це побачимо! 💖😉\nТакож у Вас є можливість запропонувати свою пісню ,яку Ви б хотіли бачити в нашому каналі! 🎧", reply_markup=kb)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'btn1':
            msg = bot.send_message(call.message.chat.id, 'Питання?\nНапишіть його сюди 🕊')
            bot.register_next_step_handler(msg, func1)
        elif call.data == 'btn2':
            msg = bot.send_message(call.message.chat.id, 'Пропозиція?\nНапишіть її сюди 🕊')
            bot.register_next_step_handler(msg, func2)
        elif call.data == 'btn3':
            msg = bot.send_message(call.message.chat.id, 'Запропонувати пісню?\nНапишіть сюди пісню яку Ви хочете почути у нашому Telegram каналі або в TikTok 🕊')
            bot.register_next_step_handler(msg, func3)


@bot.message_handler(content_types=['text'])
def func1(message):
    data = message.text
    bot.send_message(1087237679, f'Питання:\n@{message.from_user.username}\n{data}')
def func2(message):
    data = message.text
    bot.send_message(1087237679, f'Пропозиція:\n@{message.from_user.username}\n{data}')
def func3(message):
    data = message.text
    bot.send_message(1087237679, f'Запропонувати пісню:\n@{message.from_user.username}\n{data}')

bot.polling()