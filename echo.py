import telebot
bot = telebot.TeleBot("6082483452:AAHvOLNRpX7CYFByKwS2eW0OSWMlwiVEuZk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bot Is Coming, Wilujeng Rawuh")

@bot.message_handler(commands=['cekjodoh'])
def send_welcome(message):
	bot.reply_to(message, "Emang ada yang mau?")

@bot.message_handler(commands=['cekjanda'])
def send_welcome(message):
	bot.reply_to(message, "Nih bang")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
