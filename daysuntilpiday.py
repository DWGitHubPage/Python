# Python 3.9.5
# Calculating days until Pi Day next year.

import datetime


def holiday():
    PiDay = datetime.datetime(2022, 3, 14)
    return PiDay


def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(2022, 3, 14)
    delta = date2 - date1
    
    return delta

def show_info(self):
    pass

x = holiday()
now = datetime.datetime.now()
y = calculate_dates(x, now)

print("Days until Pi Day:")
print(y)


