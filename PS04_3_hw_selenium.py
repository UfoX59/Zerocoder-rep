from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search_wikipedia(browser, query):
    """Выполняет поиск статьи в Википедии по запросу"""
    browser.get('https://ru.wikipedia.org')
    search_box = browser.find_element(By.ID, 'searchInput')
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    if 'ru.wikipedia.org/wiki/' in browser.current_url:
        return True
    else:
        try:
            first_result = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.mw-search-result-heading a'))
            )
            first_result.click()
            time.sleep(2)
            return True
        except:
            return False


def get_paragraphs(browser):
    """Извлекает параграфы из основной статьи"""
    try:
        content = browser.find_element(By.ID, 'mw-content-text')
        paragraphs = content.find_elements(By.TAG_NAME, 'p')
        return [p.text for p in paragraphs if p.text.strip()]
    except:
        return []


def get_related_links(browser):
    """Собирает связанные ссылки из разделов hatnote"""
    related = []
    elements = browser.find_elements(By.CSS_SELECTOR, 'div.hatnote')
    for el in elements:
        link = el.find_elements(By.TAG_NAME, 'a')
        if link:
            related.append((link[0].text, link[0].get_attribute('href')))
    return related


def main_loop():
    """Основной цикл взаимодействия с пользователем"""
    browser = webdriver.Firefox()

    try:
        # Шаг 1: Получение первоначального запроса
        query = input("Введите поисковый запрос: ")
        if not search_wikipedia(browser, query):
            print("Статья не найдена!")
            return

        while True:
            # Шаг 3: Меню действий
            print("\nВыберите действие:")
            print("1. Читать статью")
            print("2. Перейти на связанную страницу")
            print("3. Выход")
            choice = input("> ")

            if choice == '1':
                # Листание параграфов
                paragraphs = get_paragraphs(browser)
                for i, p in enumerate(paragraphs, 1):
                    print(f"\n[Параграф {i}]\n{p}")
                    if i < len(paragraphs):
                        cont = input("\nДалее? (д/н): ").lower()
                        if cont != 'д':
                            break

            elif choice == '2':
                # Переход по ссылкам
                links = get_related_links(browser)
                if not links:
                    print("Нет доступных связанных статей!")
                    continue

                print("\nДоступные статьи:")
                for i, (title, _) in enumerate(links, 1):
                    print(f"{i}. {title}")

                try:
                    selection = int(input("\nВведите номер статьи: "))
                    if 1 <= selection <= len(links):
                        browser.get(links[selection - 1][1])
                        print(f"\nПереходим: {links[selection - 1][0]}")
                        time.sleep(2)
                    else:
                        print("Неверный номер!")
                except:
                    print("Ошибка ввода!")

            elif choice == '3':
                print("До свидания!")
                break

            else:
                print("Неверный выбор!")

    finally:
        browser.quit()


if __name__ == "__main__":
    main_loop()