# Python 3.7.1
from newspaper import Article

article = Article("https://www.cnn.com/2019/01/05/tech/ces-2019-preview/index.html")
article.download()
article.parse()

print('\n')
print(article.title)
print('\n')
print(article.authors)
print('\n') 
print(article.keywords)
print('\n')
print(article.text) 
