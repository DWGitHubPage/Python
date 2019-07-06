import datetime


def holiday():
    halloween = datetime.datetime(2019, 10, 31)
    return halloween


def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta = date2 - date1
    
    return delta

def show_info(self):
    pass

x = holiday()
now = datetime.datetime.now()
y = calculate_dates(x, now)
print("Days until Halloween:")
print(y)
