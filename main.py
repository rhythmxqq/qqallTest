import threading

import telebot
from telebot import types
import telegram
import time


bot = telebot.TeleBot('5863167978:AAFLNgkRkiFQKqhBQjhwM76yDeRKM58F5WA')
bot.set_webhook()
messages = ["Раскованная, вкусная жизнь начинается с навыка чувствовать тело. 🍓Тело диктует все, оно никогда не врет и очень важно найти контакт с телом и научиться его принимать.Без этого все остальное просто не сработает \n \nВ следующей статье я рассказала, как прийти к чувствительному телу и раскрыть внутреннюю женщину на максимум при помощи конкретных инструментов",
            "Пиши кодовое слово “Чувствительность”, чтобы получить статью",
            "Войти в контакт со своим телом - важно, но если не менять свои привычки, кардинально изменить жизнь не получится. В следующей статье ты узнаешь, какие действия необходимо предпринять, чтобы не просто немного улучшить состояние, а действительно прийти к жизни мечты 👇👇👇\n \nКак переcтать тащить все и всех на своих плечах, научиться просить и принимать как девочка, чтобы жить яркую жизнь женщины, а не ломовой лошади💪\n \n👇👇👇\nhttps://checkered-daphne-b55.notion.site/c-ee9dfd76b1d44d74be59475a83d93046",
            "Ты узнала стратегию, благодаря которой ты сможешь раскрыть свою внутреннюю женщину и притянуть в жизнь все, что пожелаешь. Но каждая ситуация очень индивидуальная и каждой нужны свои инструменты. \n\n ❗️Разобраться в том, как быстрее всего прийти к жизни мечты именно тебе, я помогаю на своих бесплатных разборах. \n\nЧтобы попасть ко мне на разбор, пиши “ЧСЧС” и мы назначим дату созвона, где я: \n🔺подсвечу причины, почему ты еще не там, где всегда мечтала быть\n🔺построю стратегию, как прийти к результату именно тебе",
            "Количество мест ограничено. Пиши “ЧСЧС” мне в личку @olaparamonova, чтобы забронировать время 🔥"]
simka = 0
counter = 0;

@bot.message_handler(commands=['start'])
def start(message):
    video = open('video.mp4', 'rb')
    bot.send_video_note(message.chat.id, video)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    continee = types.KeyboardButton("Продолжить")
    markup.add(continee)


    bot.send_message(message.chat.id, "Если:         \n1. У тебя нет мужчины или желаемых отношений\n2. Не чувствуешь себя на все 100%, тебе постоянно кажется, что с тобой что-то не так  \n3. Ты далеко не всегда испытываешь наслаждение во время секса\n4. Ты не проявляешься в мире, соответственно и отклик от мира в твоей жизни не такой уж и большой  \nТо эта видео-инструкция точно для тебя     \nПереходи, смотри и внедряй в жизнь уже сегодня, чтобы увидеть первые изменения. 👇👇👇            \nhttps://youtu.be/1en04aoJeWM",reply_markup=markup)
   # bot.send_message(message.chat.id,'Пиши кодовое слово “Чувствительность”, чтобы получить статью')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    continee = types.KeyboardButton("exit")
    markup.add(continee)
    bot.send_message(message.chat.id, "qq", reply_markup= markup)


@bot.message_handler()
def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    continee = types.KeyboardButton(text='Продолжить')
    markup.add(continee)
    global simka
    global counter
    if message.text == "Продолжить":
        if simka != 100 and counter < 2:
            bot.send_message(message.chat.id, messages[counter])
            counter += 1
        elif simka != 100 and counter == 1:

         bot.send_message(message.chat.id, "Пиши кодовое слово “Чувствительность”, чтобы получить статью", reply_markup=continee)
         counter += 1


        elif simka == 100 and counter < 5:

         bot.send_message(message.chat.id, messages[counter],reply_markup=continee)
         counter += 1


        else: #simka == 100 and counter == 4:
             bot.send_message(message.chat.id, "Нажмите повторно кнопку <<Продолжить>>, чтобы начать все сначала",reply_markup=continee)
             counter = 0
             simka = 0






    if message.text == "Чувствительность":
        simka += 100
        bot.send_message(message.chat.id,"Изучай и внедряй 👇👇👇"
                                         "\nКак перестать быть скованной, научиться чувствовать тело или почему чувствительность это фундамент сексуальности, без которого ты не раскроешь свою внутреннюю женщину на максимум?"
                                         "\n \nhttps://raspy-order-d44.notion.site/d1484610ba424dd98f8d8db442d91406",reply_markup=continee)


    if message.text == "чувствительность":
        simka += 100
        bot.send_message(message.chat.id, "Изучай и внедряй 👇👇👇"
                                          "\nКак перестать быть скованной, научиться чувствовать тело или почему чувствительность это фундамент сексуальности, без которого ты не раскроешь свою внутреннюю женщину на максимум?"
                                          "\n\nhttps://raspy-order-d44.notion.site/d1484610ba424dd98f8d8db442d91406",reply_markup=continee)












bot.polling(none_stop=True)