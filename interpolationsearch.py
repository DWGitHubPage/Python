# Python3.7.3

def interpolationSearch(arr, val):  
    low = 0
    high = (len(arr) - 1)
    while low <= high and val >= arr[low] and val <= arr[high]:
        index = low + int(((float(high - low) / ( arr[high] - arr[low]))
                         * ( val - arr[low])))
        if arr[index] == val:
            return index
        if arr[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

print("Index found at", interpolationSearch([2, 4, 6, 8, 10, 12, 14], 8))
