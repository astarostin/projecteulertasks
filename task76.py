cache = {1: 1, 2: 1, 3: 2}


def main():
	print 'Task 76'
	for n in xrange(4, 101):
		print n, count(n)
	# print count(100)


def count(n):
	if n in cache:
		return cache[n]
	num = 2
	for i in xrange(2, n - 1):
		num += count(i)
		if i <= n / 2:
			num += 1
	cache[n] = num
	return num


if __name__ == '__main__':
	main()
