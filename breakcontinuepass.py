# Python3.7.3
# Break, continue, & pass statements.


i = 0
for i in range(10):
    print(i)
    if i > 5:
        break
    else:
        print("hello")

    print("Please come here")


for i in range(10):
    print(i)
    if i > 5:
        continue
    else:
        print("Hello")

    print("Please come here, I amm lonely")

for i in range(10):
    print(i)
    if i > 5:
        pass
    else:
        print("Hello")

    print("Please come here, I amm lonely")


number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      break    # break here

   print('Number is ' + str(number))

print('Out of loop')

number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      continue    # continue here

   print('Number is ' + str(number))

print('Out of loop')

number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      pass    # pass here

   print('Number is ' + str(number))

print('Out of loop')

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
num_sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1 
    if count == 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)

num_sum = 0
count = 0
while(count<10):
    num_sum = num_sum + count
    count = count + 1 
    if count== 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)

for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)
