import telebot
from game import Game



API_KEY = '1615090323:AAFQel1syec9tyTSOPG6YDzB3yc3STnr4lU'
bot = telebot.TeleBot(API_KEY)

GAME_LIST = dict()
value = 9
value_2 = 0
wrong = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет Муха, чтобы начать игру введи команду /start_game")

@bot.message_handler(commands=['start_game'])
def send_welcome(message):
	msg = bot.send_message(message.chat.id, "Я загадал слово попробуй отгадай")
	bot.register_next_step_handler(msg, game_handler)

def game_handler(message):
	chat_id = message.chat.id
	if chat_id not in GAME_LIST:
		GAME_LIST[chat_id] = Game()
		wrong[chat_id] = []
	if GAME_LIST[chat_id].last_message:
		bot.delete_message(chat_id, GAME_LIST[chat_id].last_message)

	# if GAME_LIST[chat_id].check_lose():
	# 	bot.send_message(message.chat.id, ' you lose!!')
	# 	bot.send_message(chat_id, f'правильный ответ {GAME_LIST[chat_id].word}')
	# 	return

	GAME_LIST[chat_id].find_word(message.text)

	if GAME_LIST[chat_id].chech_win():
		bot.send_photo(message.chat.id, open(r'C:\Users\genry\Desktop\python\gallows-main\img\you win.jpg', 'rb'))
		GAME_LIST[chat_id] = Game()
		wrong[chat_id] = []
		return

	text = f'это подсказка({GAME_LIST[chat_id].word}), ({GAME_LIST[chat_id].tmp_string}) в этом слове {len(GAME_LIST[chat_id].word)} букв'
	x = value - GAME_LIST[chat_id].attempts
	if x == 0:
		# bot.send_message(message.chat.id, ' you lose!!')
		# bot.send_message(chat_id, f'правильный ответ {GAME_LIST[chat_id].word}')
		bot.send_photo(message.chat.id, open(GAME_LIST[chat_id].get_img(), 'rb'), f' you lose!!\nправильный ответ {GAME_LIST[chat_id].word}')
		GAME_LIST[chat_id] = Game()
		wrong[chat_id] = []
		return
	if str(message.text).lower() in wrong[chat_id]:
		if message.text.lower() not in GAME_LIST[chat_id].tmp_string:
			bot.send_message(chat_id, 'эта буква уже была')
			x += 1
			GAME_LIST[chat_id].attempts -= 1
		else:
			bot.send_message(chat_id, 'эта буква уже была')
	msg = bot.send_photo(message.chat.id,open(GAME_LIST[chat_id].get_img(), 'rb'), text)
	GAME_LIST[chat_id].last_message = msg.message_id
	bot.send_message(message.chat.id, f'у вас осталось {x} попыток')
	if GAME_LIST[chat_id].tmp_string.count(str(message.text).lower()) > 0:
		if str(message.text).lower() not in wrong[chat_id]:
			wrong[chat_id].append(message.text.lower())
	if GAME_LIST[chat_id].tmp_string.count(str(message.text).lower()) == 0:
		if str(message.text).lower() not in wrong[chat_id]:
			wrong[chat_id].append(message.text.lower())
	bot.send_message(chat_id, f'эти буквы уже были >>> {wrong[chat_id]}')
	bot.register_next_step_handler(msg, game_handler)




@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет user, чтобы начать игру введи команду /start_game")




bot.polling()
