# Python3.7.3
# Four methods.


# Method 1.

test_str = "pneumonoultramicroscopicsilicovolcanoconiosis"
   
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
print ("Count of all the characters in the longest word in a major dictionary:\n"
                                        +  str(all_freq)) 
print('\n')


# Method 2.

from collections import Counter 
  
test_str = "honorificabilitudinitatibus"
  
res = Counter(test_str) 
    
print("Count of the longest word used in any of Shakespeare's works:\n "
                                           +  str(res)) 
print('\n')


# Method 3.

test_str = """lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosi
    lphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryon
    optekephalliokigklopeleiolagoiosiraiobaphetraganopterygon"""
  
res = {} 
  
for keys in test_str: 
    res[keys] = res.get(keys, 0) + 1
   
print("""Count of all characters in the longest word 
to appear in literature, Aristophanes comedy, "Assemblywomen": \n"""
                                             +  str(res)) 
print('\n')


# Method 4.

test_str = "subductisupercilicarptor"
  
res = {i : test_str.count(i) for i in set(test_str)} 
  
print ("""Count of all characters in the longest word in Latin 
which means "an ultra-critical person":\n """
                                               +  str(res)) 