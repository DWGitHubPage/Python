# Python3.7.3

def gcd(a, b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b, a%b) 

# Put the numbers you want to find the gcd of as a and b.
a = 30
b= 465
   
print (f"The gcd of {a} and {b} is:") 
print (gcd(a,b)) 
