# Python 3.10.
# Convert standard time to military time.

def convert24(str1):
      
    # Check if last two elements of time is AM & first two elements are 12.
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
          
    # To remove am.    
    elif str1[-2:] == "AM":
        return str1[:-2]
      
    # Check if last two elements of time is PM and first two elements are 12.  
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
          
    else:
        # Add 12 & remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
  
# Put the standard time that you want to convert below:
print(convert24("08:05:45 PM"))
