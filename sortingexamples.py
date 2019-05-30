# Python3.7.3
# Different types of sorting.


x = [2, 4, 5, 3, 66, 77, 54, 8, 9]
print("Sorted list returned:", (sorted(x)))

print("\nReverse sort:", (sorted(x, reverse = True)))

print("\nOriginal list not modified:", (x))


# Example 2.

y = ["a", "bb", "ccccc", "dd", "aaa", "b"]

print("\nNormal sort:", (sorted(y)))
print("\nSort by length:", (sorted(y, key = len)))


# Example 3 with numbers.

def func(p):
    return p % 4

o = [12, 4, 40, 440]

print("\nNormal sort:", (sorted(o)))
print("\nSorted with key:", (sorted(o, key = func)))


# Example 4 with two lists combined.

list1 = [1, 3, 2, 66, 44, 33]
list2 = [6, 4, 5, 65, 43, 32]
c = sorted(list1 + list2)

print("\nList 1:" + str(list1))
print("\nList 2:" + str(list2))
print("\nCombining both lists:", str(c))
