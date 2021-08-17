# se utilizan las librerías de request y BeautifulSoup
import requests
from bs4 import BeautifulSoup

# se solicita el contenido de una página web
url = 'https://www.newgame.cl/hijo/pc/15/Teclados'
r = requests.get(url)
# BeautifulSoup(<Unicode or Byte>, [parser])
html_doc = BeautifulSoup(r.text, 'lxml')

# se navega por el archivo y se almacena el nombre y el precio de 
# los teclados en una lista de tuplas.
productos = html_doc.find('div', class_='array-productos')
data = []
producto = productos.find_all('a')
for info in producto:
    nombre = info.find('div', class_='juego-name').text
    precio = info.find('div', class_='juego-precio borders6').text
    precio = float(precio.replace('$', ''))
    data.append((nombre, precio))
# las tuplas se ordenen de forma decreciente en función de su precio
data.sort(key=lambda x:x[1])

# se escribe un fichero a partir de la data
f = open("./scrapNewGame.csv", "w+")
f.write("Teclado,precio\n")
for teclado in data:
    f.write("{},{}\n".format(teclado[0], teclado[1]))
f.close()