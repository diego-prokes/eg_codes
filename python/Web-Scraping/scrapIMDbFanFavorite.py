# No se puede hacer hacer web scraping de imdb

import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/what-to-watch/fan-favorites/?ref_=watch_pop_tab'
parser = 'lxml'
encoding='utf-8'
try:
    r = requests.get(url)
    # conviene pasarle el parámetro r.content y el from_encoding, para que transfome bien el texto
    soup = BeautifulSoup(r.content, parser, from_encoding=encoding)
    # de no pasarle from_encoding, el constructor lo adivinará
    # print(soup.original_encoding)
    bigContainer = soup.body.find('div', id='__next')
    main = bigContainer.main
    mediumContainer = main.find('section', class_='ipc-page-background ipc-page-background--baseAlt WhatToWatchPage__StyledPageBackground-sc-3jtrjo-0 bvejgz')
    littleContainer = mediumContainer.section.section
    divs = littleContainer.find_all('div')
    print(divs[1])
   
except ValueError:
    print(ValueError)