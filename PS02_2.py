import requests

img = 'https://sun3-20.userapi.com/impf/tKfqUOY5jCexFf3UM_r5l-qCVzKJt4W5d4IFkg/3ep5qJ2bP2s.jpg?size=1590x400&quality=95&crop=0,73,1000,251&sign=56154ecc447c40a8f7a6895d8850e466&type=cover_group'
response = requests.get(img)
with open("test.jpg", "wb") as file:
    file.write(response.content)
