import utils_calendar


def main():
	print 'task 19'
	count = 0
	per = 7
	(day, month, year) = (31, 12, 1899)

	while year < 2001:
		(day, month, year) = utils_calendar.add_calendar_period(day, month, year, per)
		if year > 1900 and day == 1:
			count += 1

	print count


if __name__ == '__main__':
	main()
