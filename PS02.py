import pprint

import requests

response = requests.get('https://api.github.com/')
print(response.status_code)
print(response.ok)
if response.ok:
    print("запрос успешно выполнен")
else:
    print("произошла ошибка")

# print(response.text)
# print(response.content)
response_json = response.json()
print(response_json)
pprint.pprint(response_json)