import telebot
import main

bot = telebot.TeleBot('8588015606:AAH0nncO4r7RzZPNiIjEhyb6IvjBrq-ozhA')
my_id = 805898147

def def_telegram():
    @bot.message_handler(content_types=['text'])
    def send(msg):
        main.send_command(msg.text.lower(), tg= True, chat= my_id)
    bot.polling(none_stop=True)