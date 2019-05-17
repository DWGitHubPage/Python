# Python3.7.3
# Cleaner & better practices to write code.


# Ternary conditionals.

condition = True

if condition:
    x = 1
else:
    x = 0

# Best to write it this way.

x = 1 if condition else 0

print(x)


# Writing large numbers in a way to be more readable with underscores.

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2


# To include comma's write it like this.
print(f'{total:,}')


# Using Context Managers.

f = open('test.txt', 'r')

file_contents = f.read()

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)


# Better to write it this way and not have to manually close down file.

with open('test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)


# Using enumerate function.

names = ['Corey', 'Christy', 'Dana', 'Jennifer']

index = 0
for name in names:
    print(index, name)
    index += 1


# Cleaner to use enumerate & how to start at 1 instead of 0.

names = ['Corey', 'Christy', 'Dana', 'Jennifer']

for index, name in enumerate(names, start=1):
    print(index, name)


# Loop over both lists.

names = ['Phil Elvrum', 'Bret Lunsford', 'Iggy Pop', 'Kim Gordon']
heroes = ['Squirrel Girl', 'Wonder Woman', 'Moon Knight', 'Doctor Strange']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}.')


# Best to use zip function.

names = ['Phil Elvrum', 'Bret Lunsford', 'Iggy Pop', 'Kim Gordon']
heroes = ['Squirrel Girl', 'Wonder Woman', 'Moon Knight', 'Doctor Strange']

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}.')


# Adding another list.

names = ['Phil Elvrum', 'Bret Lunsford', 'Iggy Pop', 'Kim Gordon']
heroes = ['Squirrel Girl', 'Wonder Woman', 'Moon Knight', 'Doctor Strange']
universes = ['Marvel', 'DC', 'Marvel', 'Marvel']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}.')


# Unpacking using underscore to cancel out variable that you don't want to use.

a, _ = (1, 2)

print(a)

# Using asterik to cancel out extra values.

a, b, *_ = (1, 2, 3, 4, 5)

print(a)
print(b)


# Canceling out variables & values.

a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)

print(a)
print(b)
#print(c)
print(d)

# Setting attributes for an object.

class Person():
    pass

person = Person()

person.first = "Corey"
person.last = "Schafer"

print(person.first)
print(person.last)


# Instead write using setattr & getattr.

class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val)

first = getattr(person, first_key)

print(person.first)


# Setattr & getattr.

class Person():
    pass

person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

# Using getattr.

for key in person_info.keys():
    print(getattr(person, key))


# Inputing secret info.

username = input('Username: ')
password = input('Password: ')

print('Logging in...')


# Better way to not show password on screen using getpass.

from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')

print('Logging in...')
