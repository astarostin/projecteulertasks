def main():
	lim = 1000000
	max_len = 0
	num = 0

	for n in range(lim, lim // 2, -1):
		cur = calc(n)
		if cur > max_len:
			max_len = cur
			num = n

	print 'num = %d, max_len = %d' % (num, max_len)


def calc(n):
	res = 1
	while n != 1:
		if n % 2 == 0:
			n //= 2
		else:
			n = 3*n + 1
		res += 1
	return res


if __name__ == '__main__':
	main()
