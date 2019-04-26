# Python3.7.3

def interpolationSearch(arr, n, x): 
    low = 0
    high = (n - 1) 

    while low <= high and x >= arr[low] and x <= arr[high]: 
        if low == high: 
            if arr[low] == x:  
                return low; 
            return -1; 
           
        pos  = low + int(((float(high - low) / 
            ( arr[high] - arr[low])) * ( x - arr[low]))) 
  
        if arr[pos] == x: 
            return pos 
   
        if arr[pos] < x: 
            low = pos + 1; 
        else: 
            high = pos - 1; 
    return -1

arr = [10, 12, 13, 16, 18, 20, 22, 24, 28, 35, 40, 45] 
n = len(arr) 
  
x = 28 # Element to look for.
index = interpolationSearch(arr, n, x) 
  
if index != -1: 
    print ("Element found at index",index) 
else: 
    print ("Element not found")
