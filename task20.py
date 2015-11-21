import utils


def main():
	print 'task 20'
	res = 0
	s = str(utils.fact(100))
	for c in s:
		res += int(c)

	print res


if __name__ == '__main__':
	main()
