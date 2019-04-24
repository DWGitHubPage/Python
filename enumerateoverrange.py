# Python3.7.3


"""Prefer using enumerate instead of range."""

flavor_list = ['chocolate', 'mint', 'pecan', 'strawberry']

for flavor in flavor_list:
    print('%s is delicious' % flavor)


for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))


for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))


for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))

# Enumerating a list.
l = ['apples', 'bananas', 'kiwi', 'oranges']
for idx, val in enumerate(l):
    print("index is %d and value is %s" % (idx, val))

# Enumerating a tuple.
r = ('apples', 'bananas', 'kiwi', 'oranges')
for idx, val in enumerate(r):
    print("index is %d and value is %s" % (idx, val))

# Enumerating a list of tuples.
a = [('Mary', 28), ('Karen', 45), ('Elle', 54)]

for idx, val in enumerate(a):
    name = val[0]
    age = val[1]
    print("index is %d, name is %s, and age is %d" \
          % (idx, name, age))

# With tuple unpacking.
for idx, (name, age) in enumerate(a):
    print("index is %d, name is %s, and age is %d" \
          % (idx, name, age))

# Enumerating a string object.
str = "Summer"

for idx, ch in enumerate(str):
    print("index is %d and character is %s" \
          % (idx, ch))

# Enumerate with a different starting index.
r = ['apples', 'bananas', 'kiwi']
for idx, s in enumerate(r, start = 1):
    print("index is %d and value is %s" \
          % (idx, s))
