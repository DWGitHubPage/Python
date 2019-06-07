# Python3.7.3
# Difference between str() & repr().

"""
Goal of str() is to be readable & more for customers.
Goal of repr() is to be unambiguous, aims at complete string representation
of the object, & is more for developers."""

import datetime
import pytz

a = [1, 2, 3, 4]
b = "string"

print(str(a))
print (repr(a))

print(str(b)) # Doesn't have quotes around it.
print(repr(b))

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print("str(a): {}".format(str(a)))
print("str(b): {}".format(str(b)))

print("repr(a): {}".format(repr(a)))
print("repr(b): {}".format(repr(b)))


today = datetime.datetime.now()
print(str(today))
print(repr(today))


class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return '(' + str(self.__num) + '/' + str(self.__den) + ')'

    def __repr__(self):
        return 'Fraction (' + str(self.__num) + ',' + str(self.__den) + ')'



f = Fraction(1,2)
print("I want to represent the fraction string as " + str(f)) 
print("I want to represent the fraction object as ", repr(f))
