import requests
from bs4 import BeautifulSoup

data = []
r = requests.get('https://www.newgame.cl/hijo/pc/15/Teclados')
html_doc = BeautifulSoup(r.text, 'lxml')
productos = html_doc.find('div', class_='array-productos')

producto = productos.find_all('a')
for info in producto:
    nombre = info.find('div', class_='juego-name').text
    precio = info.find('div', class_='juego-precio borders6').text
    precio = float(precio.replace('$', ''))
    data.append((nombre, precio))

data.sort(key=lambda x:x[1])

f = open("./scrapNewGame.csv", "w+")
f.write("Teclado,precio\n")
for teclado in data:
    f.write("{},{}\n".format(teclado[0], teclado[1]))
f.close()