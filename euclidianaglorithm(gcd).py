# Python3.7.3

from math import *

"""(GCD) Greatest Common Divisor also called (HCF)
Highest Common Factor."""

def gcd(x, y, verbose=True):
	if x < y: 
		return gcd(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print('gcd is %s' % x) 
	return x

gcd(400, 333)
gcd(236, 8)
gcd(12, 300)
