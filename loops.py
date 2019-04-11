# Python3.7.3

names = ['Elsie', 'Rachel', 'Matthew']
colors = ['orange', 'red', 'green', 'blue', 'gold', 'yellow']

for color in colors:
    print(color)

# Print backwards.

#An uglier way.

for i in range(len(colors)-1, -1, -1):
    print(colors[i])

# A cleaner way.

for color in reversed(colors):
    print(color)  

# Looping over a collection of indices.

for i, color in enumerate(colors):
    print (i, '-->', colors[i])

# Uglier way.

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])

# A Cleaner way.

for name, color in zip(names, colors):
    print(name, '-->', color)

# Loop in sorted order.

for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)

# Custom sort order.

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print(sorted(colors, key=len))
