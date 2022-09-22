# Python 3.10.0
# Getting the date and time of a location around the world.


from datetime import datetime
import pytz

datetime_in_Lagos = datetime.now(pytz.timezone('Australia/Sydney'))

print(datetime_in_Lagos)


'''Continents you can use are Africa, America for North and South America,
Asia, Atlantic, Australia, Pacific, and Europe for most areas.'''

# Documentation for the pytz library: http://pytz.sourceforge.net
