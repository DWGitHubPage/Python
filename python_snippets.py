# Python3.7.3
# Python Snippets.

"""
1. Bcrypt Password Generator  
2. Breakpoint Syntax 
3. Built-in LRU cache 
4. Bz2
5. Color Gradient Pixels 
6. Create a Single String From All Elements in a Variable
7. Data Classes 
8. Enumeration 
9. F-Strings 
10. Get hostname
11. Get ip address of website
12. Grouping Data by Attributes
13. Hash Examples 
14. Help with a File 
15. Howdoi 
16. Insert Into a List 
17. Iterable Unpacking
18. Memory Usage of an Object
19. Opening URL's
20. Pathlib
21. Path of a Module 
22. Pretty Printing 
23. Print Recursive Count of Lines of Python Source Code From Directory & Print Total Sloc.
24. Print Words Multiple Times with One Line of Code 
25. Remove a file
26. Removing Duplicates 
27. Secret Key for Flask App 
28. Sep Parameters
29. Storing Values in a List with New Variables
30. Timeit 
31. Trees on of Files & Directories in Terminal 
32. Type Hinting 
33. Version of Python
"""

# 1. Bcrypt Password Generator.

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')


# 2. Breakpoint syntax.

import pdb; pdb.set_trace()


# 3. Built-in LRU cache.

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


# 4. Bz2.

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


# 5. Color Gradient Pixels.

from PIL import Image

colors = Image.new('RGB', (276, 276), "black")

pixels = colors.load()

for x in range(0, 276):
    for y in range(0, 276):

        pixels[x, y] = (x, y, 127)

colors.show()
colors.save('pixels.png')


# 6. Create a Single String From All Elements in a Variable.

a = ["Moore's", "Law:", "The", "power", "of", "computers", "per", "unit",
     "cost", "doubles", "every", "24", "months"]

print(" ".join(a))



# 7. Data classes. 

"""Without the new data class type."""
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


"""The same implementation but with dataclass."""

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

print(armor)


# 8. Enumeration.

from enum import Enum, auto
class Monster(Enum):
    ZOMBIE = auto()
    WARRIOR = auto()
    BEAR = auto()
    
print(Monster.ZOMBIE)
print(Monster.BEAR)

for monster in Monster:
    print(monster)
  
  
"""Wrapping an Iterable with Enumerate."""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'kickball']
for index, item in enumerate(a):
    print (index, item)  


# 9. F-strings.

person = "Nicole"
action = "ticket"
message = '{} has logged in and is working on her first {}.'.format(
            person, action)

print(message)

person = "Nicole"
action = "ticket"
message = f'{person} has logged in and is working on her first {action}.'

print(message)


# 10. Get hostname.

import socket as s

my_hostname = s.gethostname()

print("Your hostname is: " + my_hostname)


# 11. Get ip address of website.

import socket as s

host = 'google.com'

ip = s.gethostbyname(host)

print("The ip address of " + host + " is: " + ip)


# 12. Grouping Data by Attributes.

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

   
# 13. Hash examples.

int_val = 4
str_val = 'Hash string value.'
flt_val = 24.56
  
print ("The integer hash value is : " + str(hash(int_val))) 
print ("The string hash value is : " + str(hash(str_val))) 
print ("The float hash value is : " + str(hash(flt_val))) 

print('\n')

tuple_val = (1, 2, 3, 4, 5) 
  
print ("The tuple hash value is : " + str(hash(tuple_val))) 

"""Hash of Infinity in Python Matches Pi."""
import sys

inf = float('inf')
print(hash(inf))
print(sys.hash_info.inf)


# 14. Help with a File.

import(file you want help on)
help name of file


# 15. Howdoi: Find answers to questions from the command line.

howdoi (ask whatever you would like)


# 16. Insert into a List.

list = ['one', 'two', 'three', 'five']

list.insert(3, 'four')
print (list)


"""Insert numbers into a list."""

data = [1, 2, 3, 7, 8, 9, 10, 11, 12]
data[3:3] = [4, 5, 6] # Inserting 4, 5, 6 between 3 & 7.

print(data)


# 17. Iterable Unpacking.

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


# 18. Memory Usage of an Object.
 
import sys 
x = 1
print(sys.getsizeof(x))


"""Returning an Object's Memory Address."""

x = 4
print(id(x))


# 19. Opening Url's.

import webbrowser

"""Opening from the command line."""

python -m webbrowser -t "https://alistapart.com"

"""Opening URL's in editor."""

"""The latest news about Python on HackerNews."""

url = 'https://hn.algolia.com/?query=python&sort=byDate&prefix&page=0&dateRange=all&type=story'

"""Open URL in a new tab, if a browser window is already open."""

webbrowser.open_new_tab(url)

"""Open URL in new window, raising the window if possible."""

webbrowser.open_new(url)


# 20. Pathlib.

from pathlib import Path

root = Path('post_sub_folder')
print(root)

"""Post_sub_folder."""

path = root / 'happy_user'

"""Make the path absolute."""

print(path.resolve())


# 21. Path of a Module.

import a_module
print(a_module.__file__)


# 22. Pretty Printing.

import pprint as pp
animals = [{'animal': 'dog', 'legs': 4, 'breeds': ['Border Collie',
           'Pit Bull', 'Huskie']}, {'animal': 'cat', 'legs': 4, 'breeds':
           ['Siamese', 'Persian', 'Sphynx']}]
pp.pprint(animals, width=1)


# 23. Print Recursive Count of Lines of Python Source Code From My Directory & Prints Total Sloc.

import sys
import os

cur_path = os.getcwd()
ignore_set = set(["__init__.py", "count_sourcelines.py"])


# 24. Print Words Multiple Times With One Line of Code.

print("happy "*2+' '+"joy "*2)


# Secret key for flask app.

import os
os.urandom(24) # Or whatever length of a key you want.

# To create a hex string (to possibly store in a JSON file).

print(os.urandom(24).hex())

# Then put that key in your __init__.py file

app.config['SECRET_KEY']='\x88\xb7\x0b\xf2%\x18yyP\x01\xd8H\xcd\x87\x101'


"""Create a secret key using secrets library."""

import secrets

secrets.token_urlsafe(16)


# 25. Remove a file.

import os
os.remove(whatever_file.py)


# 26. Removing duplicates

from collections import OrderedDict

x = [1, 2, 3, 4, 4, 3, 6, 2, 7]
print(list(OrderedDict.fromkeys(x)))


# 27. Secret key for flask app.

import os

os.urandom(24) # Or whatever length of a key you want.

"""Then put that key in your __init__.py file"""

app.config['SECRET_KEY']='\x88\xb7\x0b\xf2%\x18yyP\x01\xd8H\xcd\x87\x101'
  
 
# 28. Sep paramter.

"""Printing one sentence on two lines."""

a = "Printing one sentence"
b = "on two lines."

print(a, b, sep='\n')
  
"""Combining Sep with end to print multiple items together."""
print('A','B', sep='', end='') 
print('C')    # Prints ABC


"""Disabling the softspace feature."""

print('P','y','t', 'h', 'o', 'n', sep='') 


"""Formatting a date."""

print('09','12','2016', sep='-') 


"""Including the "@" on an email."""

print('kermitthefrog','gmail.com', sep='@') 


# 29. Storing Values in a List with New Variables.

list = [1.00, 3.56, 2.789, 4.5]
a, b, c, d = list

print(a)
print(b)
print(c)
print(d)


# 30. Timeit module.

import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

timeit.timeit('"-".join(map(str, range(100)))', number=10000)


# 31. Trees of Directories & Files in Terminal.

tree Desktop/Python # or
tree Desktop/Flask_Blog


# 32.Type hinting.

def sentence_has_animal(sentence: str) -> bool:
  return "animal" in sentence

print(sentence_has_animal("Donald had a farm without animals"))

def greeting(name: str) -> str:
    return'Hello ' + 'name'
 
 
# 33. Version of Python.
import sys
print("My version Number: {}".format(sys.version))
