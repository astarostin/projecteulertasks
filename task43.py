import utils


def main():
	print 'Task 43'
	data = [x for x in range(0, 10)]
	finished = False
	res = 0
	while finished is not True:
		if num(data, 1, 4) % 2 == 0 and num(data, 2, 5) % 3 == 0 and num(data, 3, 6) % 5 == 0 \
				and num(data, 4, 7) % 7 == 0 and num(data, 5, 8) % 11 == 0 and num(data, 6, 9) % 13 == 0 \
				and num(data, 7, 10) % 17 == 0:
			res += num(data, 0, 10)
		data = utils.next_perm(data)
		finished = data is None
	print res


def num(data, i, j):
	return int(''.join(str(x) for x in data[i:j]))


if __name__ == '__main__':
	main()
