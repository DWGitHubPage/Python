# Python3.7.3
# Using Logging.

import logging


"""
DEBUG: Detailed information, typically of interest only when
diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or
indicative of some problem in the near future (e.g. ‘disk space low’).
The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able
to perform some function.

CRITICAL: A serious error, indicating that the program itself may
be unable to continue running.
"""

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s;(levelname)s;%(message)s')
#logging.basicConfig(level=
#logging.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


# Using logging with a class.

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Matthews')
emp_3 = Employee('Eric', 'Matthews')
