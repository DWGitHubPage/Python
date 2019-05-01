# Python3.7.3
# Web scraper examples.

import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

len(res.text)
print(res.text[:485])


html = urlopen("https://github.com/trending").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)
