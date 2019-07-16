# Python3.7.4
# Python manipulation tips & tricks.

# Chained assignment.

x = y = z = 2
print(x, y, z)

# Chained comparison.

y = 5
print(2 < y <= 8)
print(6 < y <= 8)
print(2 < y > 4)

# Chain more than two comparisons.

x = 2
y = 8
print(0 < x < 4 < y < 16)

# Multiple assignment using tuple unpacking.

x, y, z = 2, 4, 8
print(x)
print(y)
print(z)


# Don't need same number of elements on both sides.

x, *y, z = 2, 4, 6, 7, 12
print(x)
print(y)
print(z)

# Swapping variables.

x, y = 2, 8
print(x)
print(y)
x, y = y, x
print(x)
print(y)

# Merge dictionaries by unpacking in new dict.

x = {'u': 1}
y = {'v': 2}
z = {**x, **y, 'w':4}
print(z)

# Joining strings using str.join.

x = ['u', 'v', 'z']
y = '-*-'.join(x)
print(y)

# Advance iteration when both sequence elements & corresponding indices.

for i, item in enumerate(['u', 'v', 'w'], start = 1):
    print('index:', i, 'element:', item)

# Reversed iteration.

for item in reversed(['u', 'v', 'w', 'x']):
    print(item)

# Aggregate elements using zip.

x = [1, 2, 3, 4]
y = ('a', 'b', 'c', 'd')
z = zip(y, x)

print(list(z))

# Transpose Matrices with zip.

x = [(1, 2, 3), ('a', 'b', 'c')]
y = zip(*x)
z = list(y)

print(z)

# Unique values & removing duplicates from a list using set.

x = [1, 2, 1, 3, 4, 5, 5, 6]
y = set(x)
print(y)
z = list(y)
print(z)

# Sort sequences by their first elements.

x = (1, 'v')
y = (4, 'u')
z = (2, 'w')
print(sorted([x, y, z]))

"""Sort by second element."""
print(sorted([x, y, z], key=lambda item: item[1]))

"""Similar if you reverse order."""

print(sorted([x, y, z], key=lambda item: item[1], reverse=True))

# Sort dictionaries with .items() method.

x = {'u': 4, 'w': 2, 'v':1}
print(sorted(x.items()))

"""Sorted by values instead."""
print(sorted(x.items(), key=lambda item: item[1], reverse=True))

# Raw formatted strings.

print(fr'u / n v w={2 + 8}')

# Obtain the index of the maximal(or minimal) element.

x = [2, 1, 4, 12, 8]
print(max((item, i) for i, item in enumerate(x))[1])

"""This approach returns the index of the last one."""

y =[2, 1, 4, 8, 8]
print(max((item, i) for i, item in enumerate(y))[1])

"""To get the inex of the first occurrence."""

print(-max((item, -i) for i, item in enumerate(y))[1])

"""Another nicer way."""

x = [2, 1, 4, 23, 5]
print(max(range(len(x)), key=lambda i: x[i]))

y = [2, 1, 3, 4, 6]
print(max(range(len(y)), key=lambda i: x[i]))

# Obtaining the Cartesian product.

import itertools
x, y, z = (2, 8), ['u', 'v', 'w'], {True, False}
print(list(itertools.product(x, y, z)))

# The operator for matrix multiplication.

import numpy as np

x, y = np.array([1, 3, 5]), np.array([2, 4, 6])
z = x @ y
print(z)


    


