def main():
	print 'Task 63'

	total = 0
	for k in xrange(1, 10):
		for n in xrange(100):
			if len(str(k ** n)) == n:
				total += 1
	print total


if __name__ == '__main__':
	main()
