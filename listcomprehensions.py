# Python 3.7.3


# Computing the square of each number.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

# Computing the squares of numbers divisible by 2.
even_squares = [x**2 for x in a if x % 2 ==0]
print(even_squares)

# Derivative data structure example.
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

"""Example of simplifying a matrix (a list containing other lists)
into one flat list of all cells."""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
flat = [x for row in matrix for x in row]
print(flat)

# Squaring the value of each.
squared = [[x**2 for x in row] for row in matrix]
print(squared)

# Filtering a list of numbers to only even values greater than four
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print(b)
print(c)
