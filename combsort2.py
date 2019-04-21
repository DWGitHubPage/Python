# Python3.7.3

def combsort(num):
    gap = len(num)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  
        swaps = False
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swaps = True
 
num_list = [45, 33, 5, 6, 2, 567, 543, 9, 8, 10, 20]
print("Before: ", num_list)
combsort(num_list)
print("After:  ", num_list)
  
