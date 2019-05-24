# Python3.7.3

import exrex
 
exrex.getone('(ex)r\\1')

 
list(exrex.generate('((hai){2}|world!)'))
 
exrex.getone('\d{4}-\d{4}-\d{4}-[0-9]{4}')
 
exrex.getone('(1[0-2]|0[1-9])(:[0-5]\d){2} (A|P)M')
 
exrex.count('[01]{0,9}')
 
print('\n'.join(exrex.generate('This is (a (secret|test|whisper)|an (code|lie|truth))\.')))
 
print(exrex.simplify('(ab|c|d)'))
