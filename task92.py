def main():
	print 'Task 92'

	cache = [n for n in xrange(1, 568) if chain(n) == 89]
	total = len(cache)
	for n in xrange(10000000, 567, -1):
		if nxt(n) in cache:
			total += 1
	print total


def chain(n):
	while n not in [1, 89]:
		n = nxt(n)
	return n


def nxt(n):
	res = 0
	for c in str(n):
		res += int(c) ** 2
	return res


if __name__ == '__main__':
	main()
