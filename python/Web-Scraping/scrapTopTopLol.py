import requests
from bs4 import BeautifulSoup

url = 'https://app.mobalytics.gg/lol/tier-list?iRole=TOP'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# busco el contendor de las imágenes de mejores campeones en top
img_contenedor = soup.find('div', class_='m-1sdtsj8')

# busco las tags de todas las imágenes de los campeones
img_tags = img_contenedor.find_all('img', class_='m-0')

# agrego tuplas con datos a la data
data = []
data_iterator = 1
for img_tag in img_tags:
    data.append((data_iterator, img_tag['alt'], img_tag['src']))
    data_iterator+=1

# paso la data a un archivo con extensión csv
f = open("./scrapTopTopLol.csv", "w+")
f.write("#,Nombre,Img_Link\n")
for fila in data:
    f.write("{},{},{}\n".format(fila[0],fila[1],fila[2]))
f.close()