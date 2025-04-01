import requests

response = requests.get('https://google.com')

print(response.status_code)

print(response.headers)

print(response.text)

