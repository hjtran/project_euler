from datetime import date

countSundays = 0

for yr in range(1901,2001):
    for month in range(1,13):
        if date(yr,month,1).weekday() == 6:
            countSundays += 1

print 'Number of sundays between 1/1/1901 and 12/31/2000 is %d' % (countSundays,)
