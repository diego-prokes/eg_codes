import requests
from bs4 import BeautifulSoup

r = requests.get('https://motherfuckingwebsite.com')
soup = BeautifulSoup(r.text , 'lxml')
print(soup.title)
print(soup.h1)
