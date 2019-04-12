# Python3.7.3

def search(arr, len, x): 
  
    for i in range (0, len): 
        if (arr[i] == x): 
            return i; 
    return -1; 
  
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; 
x = 10; 
len = len(arr); 
result = search(arr, len, x) 
if(result == -1): 
    print("Element is not in this array.") 
else: 
    print("Element is at index", result); 
