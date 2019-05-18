# Duck typing and Easier to ask Forgiveness than Permission(EAFP). 


class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm quacking like a duck!")

    def fly(self):
        print("I'm flapping my arms!")

def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)
    
    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)



person = {'name': 'Jess', 'age': 25, 'job': 'Programmer'}
#person = {'name': 'Jess', 'age': 25} # Can uncomment this out to check this way.

# Non-Pythonic.
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print("Missing some keys.")


# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))


my_list = [1, 2, 3, 4, 5, 6]

# Non-Pythonic. Asking permission is non-pythonic.
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

# Pythonic
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')


import os

my_file = "/tmp/test.txt"

# Race condition.
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File can not be accessed')

# Best to use no race-condition.
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())
    
