# Python 3.7.1
import newspaper
from newspaper import Article

article = Article("https://www.cnn.com/2018/12/18/tech/5g-mobile-att/index.html")
article.download()
article.parse()

cnn_paper = newspaper.build('http://cnn.com')

for category in cnn_paper.category_urls():
    print(category)
print('\n')
print(article.title)
print('\n')
print(article.authors)
print('\n') 
print(article.keywords)
print('\n')
print(article.text) 
