# Python3.7.3

from __future__ import print_function


def cycle_sort(array):
    ans = 0

    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]

        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        ans += 1

        while pos != cycleStart:

            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            ans += 1

    return ans


if __name__ == '__main__':
    raw_input = input  
        
user_input = raw_input('Enter numbers separated by a comma:\n')
unsorted = [int(item) for item in user_input.split(',')]
n = len(unsorted)
cycle_sort(unsorted)

print("After sort : ")
for i in range(0, n):
    print(unsorted[i], end=' ')
