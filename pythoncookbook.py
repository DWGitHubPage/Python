# Python3.7.4
# Python Cookbook Codes.


# 1.1 Unpacking a Sequence

p = (4, 5)
x, y = p
print(x, ("\r"), y)


data = ["ACME", 50, 91.1, (2019, ('July'), 14)]
name, shares, price, date = data

print(name, date)
print( price, shares)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)


s = "Hello"
a, b, c, d, e = s
print(a)
print(e)


# How to discard certain values.

data = ["ACME", 50, 91.1, (2019, ("July"), 14) ]
_, shares, price, _, = data
print(shares)
print(price)

# 1.2 Unpacking Elements from Iterables of Arbitrary Length

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

"""Example 2."""

user_record = ('Glenda', 'glenda@example.com', '773-555-1212', '856-333-5555')
name, email, *phone_numbers = user_record

print(name)
print(email)
print(phone_numbers)

"""Example 3."""

def avg_comparison(average, current):
    if average == current:
        return True
    else:
        return False

*trailing, current = sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
trailing_avg = sum(trailing) / len(trailing)
print(avg_comparison(trailing_avg, current))
print(trailing)
print(current)


"""Iterating over sequence of tuples of varying length."""

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

"""Unpacking values & throwing them away."""

record1 = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record1
print(name)
print(year)

"""Another example."""

items = [1, 10, 5, 4, 3]
head, *tail = items
print(head)
print(tail)

"""Clever recursive algorithm."""

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))


# 1.3 Keeping the Last N Items

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file.

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


# 1.4 Finding the Largest or Smallest N Items

import heapq

nums = [1, 2, 4, 55, 33, 67, 8, 4, 3, 36]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: ['price'])

cheap_q = str(cheap)[1:-1]

print(cheap_q, expensive)

"""Where items are ordered by heap.
The most important feature of a heap
is that heap[0] is always the smallest item."""

nums = [ 1, 5, 33, 6, 34, 66, 8, 78]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)

heapq.heappop(heap) # Take off from front of heap.
print(heap)


# 1.5 Implementing a Priority Queue

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())


# 1.6 Mapping Keys to Multiple Values in a Dictionary

"""Use a list if you want to preserve the insertion order of the items.
Use a set if you want to eliminate duplicates (and don’t care about
the order)."""


from collections import defaultdict


d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

f = defaultdict(list)
f['a'].append(1)
f['a'].append(2)
f['a'].append(3)
f['b'].append(4)
f['b'].append(5)

g = {}
g.setdefault('a', []).append(1)
g.setdefault('a', []).append(2)
g.setdefault('a', []).append(3)
g.setdefault('b', []).append(4)
g.setdefault('b', []).append(5)


print(d == f)
print(e == g)

def defaultdict_show():
    pairs = {
        'a': 'hello a',
        'b': 'hello b',
        'c': 'hello c'
    }

    items = {
        'a': 'hello aa',
        'b': 'hello bb',
        'c': 'hello cc'
    }

    d = defaultdict(list)
    for key, value in pairs.items():
        print(key,)
        d[key].append(value)

    for key, value in items.items():
        d[key].append(value)

    print(d)
    


defaultdict_show()


# Keeping Dictionaries in Order

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

import json

print(json.dumps(d))


# Calculating with Dictionaries


