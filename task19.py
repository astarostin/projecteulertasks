def main():
    print 'task 19'
    count = 0
    per = 7
    (day, month, year) = (31, 12, 1899)
    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
            7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    while year < 2001:
        (day, month, year) = plus_period(day, month, year, per, days)
        if year > 1900 and day == 1:
            count += 1

    print count

def plus_period(day, month, year, per, days):
    total_days = days[month]
    if leap_february(month, year):
        total_days += 1
        
    if day <= total_days - per:
        day += per
    else:
        day = per - (total_days - day)
        month += 1
        if month > 12:
            month = 1
            year += 1        
    
    return (day, month, year)

def leap_february(month, year):
    return month == 2 and leap_year(year)

def leap_year(year):
    return (year%4 == 0 and year%100 != 0) or (year%400 == 0)

if __name__ == '__main__':
	import timeit
	count=1
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)
