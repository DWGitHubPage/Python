# Python 3.9.5

import requests
from bs4 import BeautifulSoup
import json


# News from Inroads.com

def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)
        
url = 'https://inshorts.com/en/read'
response = requests.get(url)
print_headlines(response.text)

def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)

# Headlines from CNN's U.S. section.

url = "https://edition.cnn.com/US"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.findAll(attrs={'class':'cd__headline-text'}, limit=20)
for headline in headlines:
    print(headline.text)




