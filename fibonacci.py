# Python3.7.3
# Fibonacci module to use.


def fib(n):    
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

"""Then use:

import fibonacci
print(fibonacci.fib(35))

To run it up to whatever number you want."""
