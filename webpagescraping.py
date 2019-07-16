# Python3.7.4
# Scraping webpage for a certain word.

import requests
from bs4 import BeautifulSoup
 
def count_words(url, the_word):
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)
    print(words)
    return len(words)
 
 
def main():
    url = 'https://fashionmagazine.com/culture/margaret-cho-interview/'
    word = 'Cho'
    count = count_words(url, word)
    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
 
if __name__ == '__main__':
    main()
