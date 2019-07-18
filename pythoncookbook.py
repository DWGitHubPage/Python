# Python3.7.4
# Python Cookbook Ch. 1


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


# 1.7 Keeping Dictionaries in Order

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


# 1.8 Calculating with Dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print(min_price)
print(max_price)

print(min(prices.values()))
print(max(prices.values()))

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }

print(min(zip(prices.values(), prices.keys()))) 
print(max(zip(prices.values(), prices.keys())))


# 1.9 Finding Commonalities in Two Dictionaries

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# Find keys in common.
print(a.keys() & b.keys())

# Find keys in a that are not in b.
print(a.keys() - b.keys())

# Find (key, value) pairs in common.
print(a.items() & b.items())

# Make a new dictionary with certain keys removed.
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)


# 1.10 Removing Duplicates from a Sequence while Maintaining Order

# If they are hashable you can use this:
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

# Eliminating duplicates in a sequence of unhashable types:
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))


# 1.11 Naming a Slice

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)

print(items[2:4])
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]
print(items)

# Get more info. by s.start, s.stop, & s.step.

a = slice(10, 50, 2)

print(a.start)
print(a.stop)
print(a.step)


# 1.12 Determining the Most Frequently Occurring Items in a Sequence
# The collections.Counter class is designed for this problem.

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under', 'the', 'bed'
]

from collections import Counter
word_counts = Counter(words)
top_five = word_counts.most_common(5)
print(top_five)

# Count individual words.

print(word_counts['look'])
print(word_counts['into'])

# Incrementing the count manually.

morewords = ['why', 'are', 'you', 'eys', 'look', 'under', 'the', 'bed']
for word in morewords:
    word_counts[word] += 1

print(word_counts['the'])

# Another way using update() method.

word_counts.update(morewords)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

# Combine counts.

c = a + b
print(c)

# Subtracting counts.

d = a - b
print(d)


# 1.13 Sorting a List of Dictionaries by a Common Key

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# itemgetter() function can also accept multiple keys.

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# Using lambda expressions.

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))


# 1.14 Sorting Objects Without Native Comparison Support

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print(users)
print(sorted(users, key=lambda u: u.user_id))

# Another approach using attrgetter instead of lambda.

"""attrgetter is also a bit faster."""

from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

# If users had a first_name & last_name you could do this:

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))


# 1.15 Grouping Records Together Based on a Field
# Using itertools.groupby()

from operator import itemgetter
from itertools import groupby


rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('     ', i)

# Using defaultdict()

from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
        rows_by_date[row['date']].append(row)

        for r in rows_by_date['07/01/2012']:
                print(r)


# 1.16 Filtering Sequence Elements

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print(sorted(mylist))
print(sorted([n for n in mylist if n > 0]))
print(sorted([n for n in mylist if n < 0]))


# Using generator expressions to produce filtered values iteratively.

pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
        print(x)

# Putting filtering code into its own function.

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
                return False

ivals = list(filter(is_int, values))
print(sorted(ivals))

# Another example & transforming data at the same time.

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)


# Using itertools.compress() to filter.

addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
]
    
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# List of addresses where the count value is greater than 5.

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)

print(list(compress(addresses, more5)))

# 1.17 Extracting a Subset of a Dictionary

prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

# Make dictionary of prices over 200.

p1 = { key:value for key, value in prices.items() if value > 200 }

# Make dictionary of tech stocks.

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key, value in prices.items() if key in tech_names }

print(p1)
print(p2)

# Creating sequence of tuples & passing them to dict() function.

p1 = dict((key, value) for key, value in prices.items() if value > 200)

print(p1)

# Another way of writing p2.

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:prices[key] for key in prices.keys() & tech_names }

print(p2)


# 1.18 Mapping Names to Sequence Elements

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub
print(addr)
print(joined)

# Casting returned tuples to namedtuples.

def compute_cost(records):
        total = 0.0
        for rec in records:
                total += rec[1] * rec[2]
        return total

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
        total = 0.0
        for rec in records:
                s = Stock(*rec)
                total += s.shares * s.price
        return total
        
# Using namedtuple as a replacement for dictionary.

s = Stock('ACME', 100, 123.45)

print(s)

Stock(name='ACME', shares=100, price=123.45)
s = s._replace(shares=75)
print(s.shares)

# Using replace() method to populate optional or missing fields.

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
        return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}

print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))


# 1.19 Transforming and Reducing Data at the Same Time

# Calculating the sum of squares.

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

print(s)

# Other examples.

import os

files = os.listdir(os.path.expanduser('~'))
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV.

s = ('ACME', 50, 123.45)
print(', '.join(str(x) for x in s))

# Data reduction across fields of data structure.

portfolio = [
       {'name':'GOOG', 'shares': 50},
       {'name':'YHOO', 'shares': 75},
       {'name':'AOL', 'shares': 20},
       {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)

print(min_shares)

# Or you could write it this way with more info:

min_shares = min(portfolio, key=lambda s: s['shares']) 

print(min_shares)

# Same as statement above.

s = sum((x * x for x in nums))  # Pass generator -expr as argument
s = sum(x * x for x in nums)    # More elegant syntax

# Alternative to using a generator expression.

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])

print(s)

"""The generator solution above is more memory-efficient."""


# 1.20 Combining Multiple Mappings into a Single Mapping

a = { 'x': 1, 'z': 3 }
b = { 'y': 2, 'z': 4 }

# Perform lookups in both dictionaries.

from collections import ChainMap

c = ChainMap(a,b)
print(c['x'])  # Outputs from a
print(c['y'])  # Outputs from b
print(c['z'])  # Outputs from a

print(len(c))
print(sorted(list(c.keys())))
print(sorted(list(c.values())))

c['z'] = 10
c['w'] = 40
del c['x']

print(a)

# Other ways to use ChainMap.

values = ChainMap()
values['x'] = 1

print(values)

# Add new mapping

values = values.new_child()
values['x'] = 2

print(values)

# Add however many you would like

values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])  # Prints no. of mappings

# Discard last mapping

values = values.parents

print(values['x'])

# Discard another

values = values.parents

print(values['x'])
print(values)

# Alternative to ChainMap using update() method.

a = { 'x': 1, 'z': 3 }
b = { 'y': 2, 'z': 4 }

merged = dict(b)
merged.update(a)

print(merged['x'])
print(merged['y'])
print(merged['z'])

"""But it requires you to make a completely separate dictionary object"""

a['x'] = 13
print(merged['x'])

# A ChainMap uses original dictionaries so it doesn't have that behavior.

a = { 'x': 1, 'z': 3 }
b = { 'y': 2, 'z': 4 }

merged = ChainMap(a, b)
print(merged['x'])

a['x'] = 42
print(merged['x'])
