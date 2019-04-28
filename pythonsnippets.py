# Python3.7.3

#Pretty Printing
import pprint as pp
animals = [{'animal': 'dog', 'legs': 4, 'breeds': ['Border Collie',
           'Pit Bull', 'Huskie']}, {'animal': 'cat', 'legs': 4, 'breeds':
           ['Siamese', 'Persian', 'Sphynx']}]
pp.pprint(animals, width=1)


# Grouping data by attributes
from itertools import groupby

data = [
    {'animal': 'dog', 'name': 'Bella', 'age': 6},
    {'animal': 'dog', 'name': 'Neely', 'age': 4},
    {'animal': 'dog', 'name': 'Mickey', 'age': 2},
    {'animal': 'dog', 'name': 'Speck', 'age': 4},
    {'animal': 'cat', 'name': 'Mindy', 'age': 7},
    {'animal': 'cat', 'name': 'Oreo', 'age': 11},
    {'animal': 'cat', 'name': 'Ginny', 'age': 5}   
    ]

for key, group in groupby(data, lambda x: x['animal']):
    for pet in group:
        print(pet['name'] + " is a " + key)


# Removing duplicates

from collections import OrderedDict

x = [1, 2, 3, 4, 4, 3, 6, 2, 7]
print(list(OrderedDict.fromkeys(x)))


# Insert into a list
list = ['one', 'two', 'three', 'five']

list.insert(3, 'four')
print (list)


# Coloring gradient pixels

from PIL import Image

colors = Image.new('RGB', (276, 276), "black")

pixels = colors.load()

for x in range(0, 276):
    for y in range(0, 276):

        pixels[x, y] = (x, y, 127)

colors.show()
colors.save('pixels.png')
