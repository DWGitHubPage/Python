# Python3.7.3

temp = input("What is the temperature you would like to convert? (example, 45F, 82C etc.) : ")
degree = int(temp[:-1])
convention = temp[-1]

if convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  convention = "Fahrenheit"
elif convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", convention, "is", result, "degrees.")
