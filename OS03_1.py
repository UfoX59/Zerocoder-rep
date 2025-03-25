import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('')

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Отправляем ответ на любое сообщение
    bot.reply_to(message, "Этот бот лежит на локальном сервере с автозапуском")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)  # none_stop=True позволяет боту работать непрерывно