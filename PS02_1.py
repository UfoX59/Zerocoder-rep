import requests
import pprint

params = {
    'q' : 'JavaScript'
}

params1 = {
    'q' : 'python'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
response_json = response.json()

response1 = requests.get('https://api.github.com/search/repositories', params=params1)
response1_json = response1.json()
# pprint.pprint(response_json)
print(f'количество репозиториев я использованием js: {response_json['total_count']}')
print(f'количество репозиториев я использованием python: {response1_json['total_count']}')
