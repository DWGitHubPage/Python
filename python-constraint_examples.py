# Python3.7.3
"""Using python-constraint examples. 
A big thank you to https://stackabuse.com/constraint-programming-with-python-constraint/"""

import constraint


problem = constraint.Problem()

problem.addVariable('x', [1, 2, 3, 4, 5])  
problem.addVariable('y', range(20))

def our_constraint(x, y):  
    if x + y >= 5:
        return True

problem.addConstraint(our_constraint, ['x','y'])

solutions = problem.getSolutions()

length = len(solutions)  
print("(x,y) ∈ {", end="")  
for index, solution in enumerate(solutions):  
    if index == length - 1:
        print("({},{})".format(solution['x'], solution['y']), end="")
    else:
        print("({},{}),".format(solution['x'], solution['y']), end="")
print("}")



# Example 2.

print("\n")

problem.addVariables("TF", range(1, 10))  
problem.addVariables("WOUR", range(10))

# Telling Python that we need TWO + TWO = FOUR
def sum_constraint(t, w, o, f, u, r):  
    if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
        return True

"""Adding our custom constraint. The
order of variables is important."""
problem.addConstraint(sum_constraint, "TWOFUR")

"""All the characters must represent different digits,
there's a built-in constraint for that"""
problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()  
print("Number of solutions found: {}\n".format(len(solutions)))

for s in solutions:  
    print("T = {}, W = {}, O = {}, F = {}, U = {}, R = {}"
        .format(s['T'], s['W'], s['O'], s['F'], s['U'], s['R']))


# Example 3.

print("\n")

problem = constraint.Problem()

# The maximum amount of each coin type can't be more than 60
# (coin_value*num_of_coints) <= 60

problem.addVariable("1 cent", range(61))  
problem.addVariable("3 cent", range(21))  
problem.addVariable("5 cent", range(13))  
problem.addVariable("10 cent", range(7))  
problem.addVariable("20 cent", range(4))

problem.addConstraint(  
    constraint.ExactSumConstraint(60,[1,3,5,10,20]),
    ["1 cent", "3 cent", "5 cent","10 cent", "20 cent"]
)

# A function that prints out the amount of each coin
# in every acceptable combination
def print_solutions(sols):  
    for s in sols:
        print("---")
        print("""
        1 cent: {0:d}
        3 cent: {1:d}
        5 cent: {2:d}
        10 cent: {3:d}
        20 cent: {4:d}""".format(s["1 cent"], s["3 cent"],
                                 s["5 cent"], s["10 cent"], s["20 cent"]))
   
solutions = problem.getSolutions()  
print("Total number of ways: {}".format(len(solutions)))


# Example 4.

print("\n")

problem = constraint.Problem()

problem.addVariable('A', range(31))  
problem.addVariable('B', range(45))  
problem.addVariable('C', range(76))  
problem.addVariable('D', range(101))

# We have 3kg = 3,000g available
def weight_constraint(a, b, c, d):  
    if (a*100 + b*45 + c*10 + d*25) <= 3000:
        return True

# We have 1dm^3 = 1,000cm^3 available
def volume_constraint(a, b, c, d):  
    if (a*8*2.5*0.5 + b*6*2*0.5 * c*2*2*0.5 + d*3*3*0.5) <= 1000:
        return True

# We can't exceed $200
def value_constraint(a, b, c, d):  
    if (a*8 + b*6.8 + c*4 + d*3) < 300:
        return True

problem.addConstraint(weight_constraint, "ABCD")  
problem.addConstraint(volume_constraint, "ABCD")  
problem.addConstraint(value_constraint, "ABCD")

maximum_sweetness = 0  
solution_found = {}  
solutions = problem.getSolutions()

for s in solutions:  
    current_sweetness = s['A']*10 + s['B']*8 + s['C']*4.5 + s['D']*3.5
    if current_sweetness > maximum_sweetness:
        maximum_sweetness = current_sweetness
        solution_found = s

print("""The maximum sweetness we can bring is: {}  
{}g of Chocolate A,
{}g of Chocolate B,
{}g of Chocolate C,
{}g of Chocolate D
""".format(maximum_sweetness, solution_found['A'],
           solution_found['B'], solution_found['C'], solution_found['D']))


# Example 5. Sudoku.

import json

problem = constraint.Problem()

# We're letting VARIABLES 11 through 99 have an interval of [1..9]
for i in range(1, 10):  
    problem.addVariables(range(i * 10 + 1, i * 10 + 10), range(1, 10))

# We're adding the constraint that all values in a row must be different
# 11 through 19 must be different, 21 through 29 must be all different.
for i in range(1, 10):  
    problem.addConstraint(constraint.AllDifferentConstraint(),
                          range(i * 10 + 1, i * 10 + 10))

# Also all values in a column must be different
for i in range(1, 10):  
    problem.addConstraint(constraint.AllDifferentConstraint(),
                          range(10 + i, 100 + i, 10))

for i in [1,4,7]:  
    for j in [1,4,7]:
        square = [10*i+j,10*i+j+1,10*i+j+2,10*(i+1)+j,10*(i+1)+j+1,10*
                  (i+1)+j+2,10*(i+2)+j,10*(i+2)+j+1,10*(i+2)+j+2]
        problem.addConstraint(constraint.AllDifferentConstraint(), square)

file_name = input("Enter the name of the .json file containing the sudoku puzzle: ")  
f = open(file_name, "r")  
board = json.load(f)  
f.close()


for i in range(9):  
    for j in range(9):
        if board[i][j] != 0:
            def c(variable_value, value_in_table = board[i][j]):
                if variable_value == value_in_table:
                    return True
                
            problem.addConstraint(c, [((i+1)*10 + (j+1))])

solutions = problem.getSolutions()

for s in solutions:  
    print("==================")
    for i in range(1,10):
        print("|", end='')
        for j in range(1,10):
            if j%3 == 0:
                print(str(s[i*10+j])+" | ", end='')
            else:
                print(str(s[i*10+j]), end='')
        print("")
        if i%3 == 0 and i!=9:
            print("------------------")
    print("==================")

if len(solutions) == 0:  
    print("No solutions found.")
