# Python3.7.3

"""Prioritizing values and they are sorted in order,
numerically or alphabetically."""

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1, x)
    values.sort(key=helper)

numbers = [18, 30, 10, 20, 15, 14, 17, 16]
group = {20, 30, 10}
sort_priority(numbers, group)
print(numbers)


def sort_priority2(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
group = {'a', 'e', 'i'}
sort_priority2(letters, group)
print(letters)


def sort_priority3(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

words = ['burrow owl', 'rabbit', 'zebra', 'turtle', 'owl', 'penguin', 'bird']
group = {'owl', 'bird', 'zebra', 'turtle'}
sort_priority3(words, group)
print(words)

