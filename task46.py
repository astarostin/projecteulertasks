import math
import utils


primes = utils.primes_eratosthenes_bound(100000)


def main():
	print 'Task 46'

	n = 33
	while acceptable(n):
		n = next(n)		
				
	print n


def next(n):
	if n % 2 == 0:
		n += 1
	else:
		n += 2
	while n in primes:
		n += 2
	return n
	
	
def acceptable(n):
	i = 1
	sq = 2 * i * i
	while n - sq > 1:
		if (n - sq) in primes:
			return True
		i += 1
		sq = 2 * i * i
	return False

if __name__ == '__main__':
	main()
