import utils

ab_list = []


def main():
	print 'task 23'
	data = []
	lim = 28123

	for n in range(1, lim + 1):
		if has_no_abundant_parts(n):
			data.append(n)

	print sum(data)


def has_no_abundant_parts(n):
	i = 1
	res = True
	while i <= n // 2:
		if is_abundant(i) and is_abundant(n - i):
			res = False
			break
		i += 1

	return res


def is_abundant(n):
	if n in ab_list:
		return True
	if sum(utils.find_all_divisors(n, False)) > n:
		ab_list.append(n)
		return True
	return False


if __name__ == '__main__':
	main()
