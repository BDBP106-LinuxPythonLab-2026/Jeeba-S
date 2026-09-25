import calendar
def magic_date(d,m,y):
    y = y % 100
    return d * m == y

for y in range(1901,2001):
    for m in range(1,13):
        max_day=calendar.monthrange(y,m)[1]
        for d in range(1, max_day + 1):
            if magic_date(d,m,y):
                print(d,"-",m,"-",y)


