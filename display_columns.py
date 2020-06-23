# Python 3.8.2
# Printing columns of info. similar to display_columns Bash script.

import sys

f = sys.stdin
# If you need to open a file instead:
f = open('names')
for line in f:
    fields = line.strip(' ')
    # Array indices start at 0 unlike AWK
    print(fields)
