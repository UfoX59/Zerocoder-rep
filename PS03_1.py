from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
text = soup.find("span", class_="text")
print(text)

text1 = soup.find_all("span", class_="text")
print(text1)

author = soup.find_all("small", class_="author")
print(author)

for i in range(len(text1)):
    print(f"Цитата номер - {i+1}")
    print(text1[i].text)
    print(f"Автор цитаты - {author[i].text}\n")