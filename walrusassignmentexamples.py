# Python 3.8.0
# Using the new walrus assignment operator.


# Old way.

walrus = True
print(walrus)


# With the walrus operator.

print(walrus := True)

# Old way of doing a while loop.

classes = list()
while True:
    current = input("Write something: ")
    if current == "quit":
        break
    classes.append(current)


# Using the walrus operator.

classes = list()
while (current := input("Write something: ")) != "quit":
    classes.append(current)


# Another example of a while loop.

i = 1
while (num := i) < 10:
    print(i, "and", num, 'are the same number.')
    i = i + 1


# Another example comparing numbers.

number = 50
if number > 40:
    print(number, "is greater than 40.")


# Using the walrus operator.

if (number := 50) > 40:
    print(number, "is greater than 40.")
