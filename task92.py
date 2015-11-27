def main():
	print 'Task 92'

	total = 0
	for n in xrange(10000000, 0, -1):
		if chain(n) == 89:
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
