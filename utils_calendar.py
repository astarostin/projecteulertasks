DAYS_OF_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def add_calendar_period(day, month, year, per):
	""" Add given amount of days to given date
	:param day:
	:param month:
	:param year:
	:param per: amount of days to add
	:return: new date
	"""
	total_days = DAYS_OF_MONTHS[month]
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

	return day, month, year


def leap_february(month, year):
	return month == 2 and leap_year(year)


def leap_year(year):
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
