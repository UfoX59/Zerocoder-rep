# по причине несовместимости версий интерпретатора и версии googletrans из урока, пришлось использовать deep_translator
# пробовал сменить интерпретатор на 3.12, обновил какие-то модули, но всё равно не запустилось, решил не тратить много времени на решение проблемы
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
import requests

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
#        print(response.text)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
#        translator = GoogleTranslator(sourse="auto", target="ru")
#        for word in english_words:
#            russian_words = translator.translate(english_words[word])
#            print (russian_words[word])

        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words").lower()
        word_definition = word_dict.get("word_definition").lower()
        translator = GoogleTranslator(sourse="auto", target="ru")
        word_rus = translator.translate(word_dict.get("english_words")).lower()
        word_definition_rus = translator.translate(word_dict.get("word_definition")).lower()
#       print(word_dict)
#       print(word_definition_rus)
        print (word)
        print (word_rus)

        print(f"Значение слова - {word_definition}")
        print(f"Значение слова - {word_definition_rus}")

        user_rus = input("Что это за слово? ").lower()
        translator = GoogleTranslator(sourse="auto", target="en")
        user_eng = translator.translate(user_rus).lower()
        print(user_eng)

        if user_eng == word:
            print("Всё верно!")
        else:
            print(f"ответ неверный, было загадано слово - {word}")

        play_again = input("Хотите сыграть ещё раз? y/n ")
        if play_again != "y" and play_again != "н":
            print("Спасибо за игру!")
            break

word_game()
