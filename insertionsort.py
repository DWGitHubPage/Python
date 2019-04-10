# Python.3.7.3

from __future__ import print_function

def insertion_sort(collection):
    for index in range(1, len(collection)):
        while index > 0 and collection[index - 1] > collection[index]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection

if __name__ == '__main__':
    try:
        raw_input          
    except NameError:
        raw_input = input  

    user_input = raw_input('Enter numbers that you want to sort, separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))
