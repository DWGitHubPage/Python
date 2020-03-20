# Python 3.8.2
# Pinging script.

import os

hostnames = [
    '8.8.8.8', # Google DNS.
    '127.0.0.1', # Loopback address to know if network adapter is working.
    '255.255.255.255' # Broadcast address, "this network."
]

for hostname in hostnames:
    response = os.system('ping -c 2 ' + hostname)
    if response == 0:
        print (hostname, 'is up.')
    else:
        print (hostname, 'is down.')
