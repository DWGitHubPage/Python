#Python3.7.3
import pandas as pd


data = {
    'fruit': [5, 2, 1, 8],
    'vegetables': [1, 3, 2, 7]
}

purchases = pd.DataFrame(data, index=['John', 'Michelle', 'Marc', 'Barbara'])

print(purchases.loc['Michelle'])
print('\n')
print(purchases)
