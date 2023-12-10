from log import log
from threading import Thread
from random import randint as rand

log("Импорт библиотек..", "info")
try:
    import telebot
    log("Импорт библиотек успешно завершена.", "complete")
except:
    log("Библиотеки не найдены.", "error")
    log("Установка библиотек..", "warning")
    from os import system as run
    modules = ["telebot"]
    for i in modules:
        log("Установка " + i, "info")
        run("pip install " + i)
        log("Установка пакета " + i + " успешно завершена.", "complete")
    log("Установка пакетов успешно завершена.", "complete")
    log("Перезагрузите программу для запуска библиотек.", "warning")
    exit(0)

# Токен
API_TOKEN = '6488158688:AAE18HqrPZSQ47oO32QGkydp3HUUOvySZNY'

log("Создание обьекта bot", "info") #log
bot = telebot.TeleBot(API_TOKEN) #Создание экземпляра бота
log("Экземпляр обьекта bot создан", "complete") #log

log("Создание функций обработки сообщений", "info") #log

#Основная обработка
def mess(message):
    return message.text;

@bot.message_handler(func=mess) #Обработка сообщения при /start
def start(message):
    log("[" + str(message.chat.username) + "]: " + str(message.text), "info")

log("Функции бота обработаны.", "complete") #log

log("Бот запущен.", "complete") #log
bot.polling() # Запуск pool requests (проще говоря запуск цикла бота)