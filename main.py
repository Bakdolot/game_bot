import telebot
from app import Game

bot = telebot.TeleBot('1631510673:AAH8oRhSvDOllTDvQsSfxRR8c46SQWZ7Ip8')
gr = dict()
# gr[1] = Game()
#
# gr[1].find_word('а')
# print('а ->', gr[1].word, '->', gr[1].tmp_string)
# gr[1].find_word('о')
# print('о ->', gr[1].word, '->', gr[1].tmp_string)
# gr[1].find_word('в')
# print('в ->', gr[1].word, '->', gr[1].tmp_string)
# gr[1].find_word('й')
# print('й ->', gr[1].word, '->', gr[1].tmp_string)
# gr[1].find_word('е')
# print('е ->', gr[1].word, '->', gr[1].tmp_string)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, для запуска новой игры отправь /new_game')
#
# @bot.message_handler(commands=['new_game'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /new')
#
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     print(message)
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#         print(type(message.chat.id))
#     elif message.text == 'Пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#
# bot.polling()
