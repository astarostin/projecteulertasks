def main():
	print 'Task 40'
	count = 0
	n = 1
	prod = 1
	positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
	while count < 1000001:
		for i in xrange(1, len(str(n)) + 1):
			pos = count + i
			if pos in positions:
				prod *= int(str(n)[i - 1])
		count += len(str(n))
		n += 1
	print prod

if __name__ == '__main__':
	main()
