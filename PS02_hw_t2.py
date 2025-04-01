# Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params1 = {'userId': 1}

response1 = requests.get(url, params = params1)
if response1.status_code == 200:
    posts = response1.json()
    print(posts)
    for p in posts:
        print(f"Post ID: {p['id']}")
        print(f"Title: {p['title']}")
        print(f"Body: {p['body']}")
        print("---" * 10)
else:
    print(f"Ошибка запроса: {response1.status_code}")