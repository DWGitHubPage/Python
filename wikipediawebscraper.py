# Python3.7.3
# Wikipedia API scraper.

import wikipedia

print(wikipedia.search("Peter"))
print("\n")
print(wikipedia.search("Peter", results=4))
print("\n")
print(wikipedia.suggest("Peter Dinklage"))
print("\n")
print(wikipedia.summary("Python"))
print("\n")
print(wikipedia.summary("Python", sentences=2))
print("\n")
print(wikipedia.summary("Key (cryptography)"))  
print("\n")
print(wikipedia.page("Python").content)

