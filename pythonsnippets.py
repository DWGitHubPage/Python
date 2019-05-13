# Python3.7.3
"""Import sys, path of module, built-in LRU cache, f-strings, pathlib, type hinting, 
enumeration, iterable unpacking, data classes, pretty printing, grouping
data by attributes, removing duplicates, coloring gradient pixels, 
grouping data by attributes, inserting numbers into list, and hash. """

# Checking version of Python.
import sys
print("My version Number: {}".format(sys.version))


# Finding the path of a module.
import a_module
print(a_module.__file__)


# Breakpoint syntax.
import pdb; pdb.set_trace()


# Built-in LRU cache.

import time
def fib(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    
    return fib(number-1) + fib(number-2)
start = time.time()
fib(1)
print(f'Duration: {time.time() - start}s')


from functools import lru_cache
@lru_cache(maxsize=512)
def fib_memoization(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    
    return fib_memoization(number-1) + fib_memoization(number-2)
start = time.time()
fib_memoization(40)
print(f'Duration: {time.time() - start}s')


# F strings.

person = "Nicole"
action = "ticket"
message = '{} has logged in and is working on her first {}.'.format(
            person, action)

print(message)

person = "Nicole"
action = "ticket"
message = f'{person} has logged in and is working on her first {action}.'

print(message)


# Using pathlib.

from pathlib import Path

root = Path('post_sub_folder')
print(root)

# post_sub_folder
path = root / 'happy_user'

# Make the path absolute
print(path.resolve())


# Type hinting.

def sentence_has_animal(sentence: str) -> bool:
  return "animal" in sentence

print(sentence_has_animal("Donald had a farm without animals"))

def greeting(name: str) -> str:
    return'Hello ' + 'name'


# Enumeration.

from enum import Enum, auto
class Monster(Enum):
    ZOMBIE = auto()
    WARRIOR = auto()
    BEAR = auto()
    
print(Monster.ZOMBIE)
print(Monster.BEAR)

for monster in Monster:
    print(monster)


# Iterable unpacking.

head, *body, tail = range(5)
print(head, body, tail)
# 0 [1, 2, 3] 4
py, filename, *cmds = "python3.7.3 script.py -n 5 -l 15".split()
print(py)
print(filename)
print(cmds)
# python3.7.3
# script.py
# ['-n', '5', '-l', '15']
first, _, third, *_ = range(10)
print(first, third)


# Data classes 3.7

# Without the new data class type.
class Armor:
    
    def __init__(self, armor: float, description: str, level: int = 1):
        self.armor = armor
        self.level = level
        self.description = description
                 
    def power(self) -> float:
        return self.armor * self.level
    
armor = Armor(5.2, "Common armor.", 2)
armor.power()

print(armor)


# The same implementation but with dataclass.

from dataclasses import dataclass
@dataclass
class Armor:
    armor: float
    description: str
    level: int = 1
    
    def power(self) -> float:
        return self.armor * self.level
    
armor = Armor(5.2, "Common armor.", 2)
armor.power()
# 10.4
print(armor)


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


# Inserting numbers into a list.

data = [1, 2, 3, 7, 8, 9, 10, 11, 12]

data[3:3] = [4, 5, 6] # Inserting 4, 5, 6 between 3 & 7.

print(data)

"""Print recursive count of lines of python source code from my directory
and prints total sloc"""

import os


cur_path = os.getcwd()
ignore_set = set(["__init__.py", "count_sourcelines.py"])

loclist = []

for pydir, _, pyfiles in os.walk(cur_path):
    for pyfile in pyfiles:
        if pyfile.endswith(".py") and pyfile not in ignore_set:
            totalpath = os.path.join(pydir, pyfile)
            loclist.append( ( len(open(totalpath, "r").read().splitlines()),
                               totalpath.split(cur_path)[1]) )

for linenumbercount, filename in loclist: 
    print ("%05d lines in %s" % (linenumbercount, filename))

print ("\nTotal: %s lines (%s)" %(sum([x[0] for x in loclist]), cur_path))


# Hash examples.

int_val = 4
str_val = 'Hash string value.'
flt_val = 24.56
  
print ("The integer hash value is : " + str(hash(int_val))) 
print ("The string hash value is : " + str(hash(str_val))) 
print ("The float hash value is : " + str(hash(flt_val))) 

print('\n')

tuple_val = (1, 2, 3, 4, 5) 
  
print ("The tuple hash value is : " + str(hash(tuple_val))) 


# Timeit module.

import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

timeit.timeit('"-".join(map(str, range(100)))', number=10000)


# Opening url's with webbrowser library.

import webbrowser

# Opening from the command line.
python -m webbrowser -t "https://alistapart.com"

# Opening URL's.

url = 'https://news.ycombinator.com'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)



