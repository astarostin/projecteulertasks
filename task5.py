import utils


def main():
	print 'task 5'
	lim = 20
	print lcm_list(range(2, lim + 1))


def lcm_list(lst):
	if len(lst) == 0:
		return 0
	if len(lst) == 1:
		return lst[0]
	if len(lst) == 2:
		return utils.lcm(lst[0], lst[1])
	return utils.lcm(lcm_list(lst[:-1]), lst[-1])


if __name__ == '__main__':
	main()
