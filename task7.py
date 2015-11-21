import utils


def main():
	print 'task 7'
	n = 10001
	lst = utils.primes_eratosthenes_amount(n)
	print lst[-1]


if __name__ == '__main__':
	main()
