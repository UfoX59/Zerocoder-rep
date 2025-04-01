# Задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.

import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
url = 'https://jsonplaceholder.typicode.com/posts'

response3 = requests.post(url, data = data)
response3_json = response3.json()
print(response3.status_code)
print(f"Ответ: {response3_json}")
