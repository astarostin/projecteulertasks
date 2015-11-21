import utils


def main():
	print 'task 10'
	n = 2000000
	lst = utils.primes_eratosthenes_bound(n)
	
	print sum(lst)

if __name__ == '__main__':
	main()
