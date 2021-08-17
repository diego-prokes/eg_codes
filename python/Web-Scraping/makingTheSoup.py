import requests
from bs4 import BeautifulSoup

# se almacena una response
r = requests.get('https://motherfuckingwebsite.com')

# se imprimen el tipo de dato de r, r.content y r.text
print('se imprimen el tipo de dato de r, r.content y r.text')
print(type(r))
print(type(r.content))
print(type(r.text))

# se crean dos sopas, una a partir de r.content y la otra de r.text
byte_soup = BeautifulSoup(r.content, 'lxml')
str_soup = BeautifulSoup(r.text, 'lxml')
# se imprime el tipo de dato de ambas variables (resulta ser el mismo)
print(type(byte_soup))
print(type(str_soup))