# Python3.7.3

def find_max_subarray(alist, start, end):
    max_ending_at_i = max_seen_so_far = alist[start]
    max_left_at_i = max_left_so_far = start
    # max_right_at_i is always i + 1
    max_right_so_far = start + 1
    for i in range(start + 1, end):
        if max_ending_at_i > 0:
            max_ending_at_i += alist[i]
        else:
            max_ending_at_i = alist[i]
            max_left_at_i = i
        if max_ending_at_i > max_seen_so_far:
            max_seen_so_far = max_ending_at_i
            max_left_so_far = max_left_at_i
            max_right_so_far = i + 1
    return max_left_so_far, max_right_so_far, max_seen_so_far
 
alist = input("Enter the list of numbers and do not separate with comma's:")
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print("The maximum subarray starts at index {}, ends at index {}"
      " and has sum {}.".format(start, end - 1, maximum))
