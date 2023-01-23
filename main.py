import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    inf = 'Здравствуйте,Я бот Jellyfish.\n Здесь вы можете:\n 1)получить информацию о продукте \n2) Сообщить об ошибке'
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('Товары')
    item2 = types.KeyboardButton('Проблемы')
    markup.row(item1, item2)
    bot.send_message(message.chat.id, inf, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == "Назад в меню":
        start(message)
    elif message.text == 'Товары':
        markup = types.ReplyKeyboardMarkup()
        itm1 = types.KeyboardButton("Книги")
        itm2 = types.KeyboardButton("Назад в меню")
        markup.add(itm1, itm2)
        bot.send_message(message.chat.id," Товары: ",reply_markup=markup)
    elif message.text =='Проблемы':
        email = 'ulanovulukbek2@gmail.com'
        phone = 'https://wa.me/996703845973'
        bot.send_message(message.chat.id, f"Если у вас возникли проблемы с работой напишите нам! {email}\n {phone}" )
    else: 
        bot.send_message(message.chat.id, 'Вы выбрали не существующий параметр. \n Попробуйте снова!')


if __name__=='__main__':
    bot.polling(True)