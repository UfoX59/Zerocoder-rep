import requests

# Задание 1: Получение данных
params = {
    'q' : 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()

print(f'количество репозиториев c использованием html: {response_json['total_count']}')
