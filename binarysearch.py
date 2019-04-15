# Python3.7.3

def binarysearch (arr, l, r, x): 

    if r >= l: 
        mid = l + (r - l)/2
  
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarysearch(arr, l, mid-1, x) 
  
        else: 
            return binarysearch(arr, mid + 1, r, x) 
  
    else: 
        return -1
   
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
x = 10
  
result = binarysearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in the array.")