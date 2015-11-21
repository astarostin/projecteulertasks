import utils


def main():
	print 'task 24'
	s = "0123456789"
	data = [int(c) for c in s]
	count = 1
	lim = 1000000
	finished = False
	while finished is not True and count < lim:
		data = utils.next_perm(data)
		count += 1
		finished = data is None

	print reduce(lambda x, y: str(x) + str(y), data)


if __name__ == '__main__':
	main()
