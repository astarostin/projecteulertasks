import utils


def main():
	print 'task 12'
	num = 1
	step = 2
	divisors = 500

	while len(utils.find_all_divisors(num)) < divisors:
		num += step
		step += 1
	print num


if __name__ == '__main__':
	main()
