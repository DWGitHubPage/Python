# Python3.7.3
# Printing logging messages marked with the time of the logged event.

import datetime
import time
import json


def log(message, when=None):

    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))
    

log('Hi there!')
time.sleep(0.1)
log('Hi again!')


# Using JSON.

def decode(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['Ooooh'] = 5
bar = decode('also bad')
bar['Yeaaah!'] = 1
print('Foo:', foo)
print('Bar:', bar)
