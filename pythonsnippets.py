# Python3.7.3
"""bz2, bcrypt, generating secret key, help with a file, looking up attributes & methods, import sys, path of module, 
built-in LRU cache, f-strings, pathlib, type hinting, enumeration, wrapping an iterable 
with enumerate, iterable unpacking, data classes, pretty printing, grouping data by 
attributes, removing duplicates, coloring gradient pixels, grouping data by attributes, 
inserting numbers into list, check memory usage of object, howdoi, open URL's, 
hash, storing values in a list with new variables, timeit, the hash of infinity in 
Python matches pi, creating a string from all the elements in a variable, trees on command line, printing words multiple 
times with one line of code, sep parameter. """


# Bz2.

import bz2

data = b"""\
 Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
print(data)

c = bz2.compress(data)
print(len(data) / len(c)) # Data compression ratio.

d = bz2.decompress(c) 
print(data == d) # Check equality to original object after round-trip.


# Bcrypt password generator.

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')


# Generating secret key for flask app.

import os
os.urandom(24) # Or whatever length of a key you want.

# To create a hex string (to possibly store in a JSON file).

print(os.urandom(24).hex())

# Then put that key in your __init__.py file

app.config['SECRET_KEY']='\x88\xb7\x0b\xf2%\x18yyP\x01\xd8H\xcd\x87\x101'

# Create a secret key using secrets library.

import secrets

secrets.token_urlsafe(16)


# Checking version of Python.
import sys
print("My version Number: {}".format(sys.version))


# Finding the path of a module.
import a_module
print(a_module.__file__)


# Finding the absolute path for file or directory using os.

import os

os.path.abspath('fizzbuzz.py')


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

# How to get help with a file.

import(file you want help on)
help name of file

# Looking up attributes and methods.

from datetime import datetime
dir(datetime)


# Checking the memory usage of an object.
 
import sys 
x = 1
print(sys.getsizeof(x))


# Returning an object's memory address.

x = 4
print(id(x))


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
  
 
# Wrapping an iterable with enumerate.

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'kickball']
for index, item in enumerate(a):
    print (index, item)


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


# Store values in a list with new variables.

list = [1.00, 3.56, 2.789, 4.5]
a, b, c, d = list

print(a)
print(b)
print(c)
print(d)


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

# The latest news about Python on HackerNews.
url = 'https://hn.algolia.com/?query=python&sort=byDate&prefix&page=0&dateRange=all&type=story'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)


# Howdoi: Find answers to questions from the command line.

howdoi (ask whatever you woul like)


# The hash of infinity in Python matches pi.
import sys

inf = float('inf')
print(hash(inf))
print(sys.hash_info.inf)


# Create a single string from all the elements in a variable.

a = ["Moore's", "Law:", "The", "power", "of", "computers", "per", "unit",
     "cost", "doubles", "every", "24", "months"]

print(" ".join(a))


# Finding the tree of directories & files in terminal.

tree Desktop/Python # or
tree Desktop/Flask_Blog


# Print two words multiple times with one line of code.

print("happy "*2+' '+"joy "*2)


# Sep paramter.

"""Printing one sentence on two lines."""

a = "Printing one sentence"
b = "on two lines."

print(a, b, sep='\n')


"""Disabling the softspace feature."""

print('P','y','t', 'h', 'o', 'n', sep='') 


"""Formatting a date."""

print('09','12','2016', sep='-') 


"""Including the "@" on an email.
print('kermitthefrog','gmail.com', sep='@') 
  
  
"""Combining sep with end to print multiple items together."""
print('A','B', sep='', end='') 
print('C')    # Prints ABC

