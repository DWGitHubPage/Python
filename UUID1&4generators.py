# Python3.7.3
# UUID1 & UUID4 (Universal Unique Identifier) generators.

import uuid

print ("The random UUID created is: ",end="") 
print (uuid.uuid1()) 
print("\n") 


# UUID created by using uuid4()

id = uuid.uuid4() 
  
print ("The id generated using uuid4(): ",end="") 
print (id)
print("\n") 


# Components, representations & variants of uuid1().

id = uuid.uuid1() 
  
print ("The representations of uuid1() are: ") 
print ("byte representation: ",end="") 
print (repr(id.bytes)) 
  
print ("int representation: ",end="") 
print (id.int) 
  
print ("hex representation: ",end="") 
print (id.hex) 
  
print("\n") 
  
print ("The components of uuid1() are: ") 
print ("Version: ",end="") 
print (id.version) 
  
print ("Variant: ",end="") 
print (id.variant) 
  
print("\n") 
  
print ("The fields of uuid1() are: ") 
print ("Fields: ",end="") 
print (id.fields) 
  
print("\n") 
  
# Time Component of uuid1() 
print ("The time component of uuid1() is: ") 
print ("Time component: ",end="") 
print (id.node) 
