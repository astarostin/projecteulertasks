import utils


def main():
	print 'task 21'
	lim = 10000
	data = []

	for n in range(1, lim):
		if n not in data:
			dn = sum(utils.find_all_divisors(n, False))
			if n == sum(utils.find_all_divisors(dn, False)) and n != dn:
				data.append(n)
				data.append(dn)
	print sum(data)


if __name__ == '__main__':
	main()
