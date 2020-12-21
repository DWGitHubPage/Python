# Python 3.9.1
# Reversing lists examples.

# Example 1.

cables = ['RJ-11', 'RJ-45', 'DB-15', 'VGA']
print ('Original List: ', cables)

cables.reverse()
print('Updated List: ', cables)


# Example 2.

cables = ['RJ-11', 'RJ-45', 'DB-15', 'VGA']
print ('Original List: ', cables)

reversed_list = cables[::-1]
print('Updated List: ', reversed_list)


# Example 3.

cables = ['RJ-11', 'RJ-45', 'DB-15', 'VGA']

for o in cables:
    print(o)

for o in reversed(cables):
    print(o)
