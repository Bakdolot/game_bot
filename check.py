import telebot
from game import Game


API_KEY = ''

bot = telebot.TeleBot(API_KEY)

GAME_LIST = dict()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Чтобы начать игру введи /start_game")


@bot.message_handler(commands=['start_game'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Я загадал слово, попробуй отгадай")
    bot.register_next_step_handler(msg, game_handler)


def game_handler(message):
    chat_id = message.chat.id
    if chat_id not in GAME_LIST:
        GAME_LIST[chat_id] = Game()

    if GAME_LIST[chat_id].check_lose():
        bot.send_message(message.chat.id, "Вы  проиграли!")
        return

    GAME_LIST[chat_id].find_word(message.text)

    if GAME_LIST[chat_id].check_win():
        bot.send_message(message.chat.id, "Вы  отгадали слово!")
        return

    text = f"{GAME_LIST[chat_id].word} {GAME_LIST[chat_id].tmp_string}"
    bot.send_message(message.chat.id, 10 - GAME_LIST[chat_id].attempts)

    msg = bot.send_message(message.chat.id, text)

    bot.register_next_step_handler(msg, game_handler)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я не умею ничего больше)")


bot.polling()