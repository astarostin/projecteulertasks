def main():
	print 'Task 38'
	max_pan = 0
	for i in xrange(1, 100000):
		for count in xrange(1, 100):
			prod = get_concatenated_product(i, count)
			if is_pandigital(prod) and prod > max_pan:
				max_pan = prod
	print max_pan


def get_concatenated_product(n, count):
	res = ''
	for i in xrange(1, count + 1):
		res += str(n * i)
		if len(res) > 9:
			return 0
	return res


def is_pandigital(n):
	if len(str(n)) != 9:
		return False
	for i in xrange(1, 10):
		if str(i) not in str(n):
			return False
	return True

if __name__ == '__main__':
	main()
