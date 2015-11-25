import math
import utils


def main():
	print 'Task 50'
	upper_limit = 1000000
	primes = utils.primes_eratosthenes_bound(upper_limit)		
	start = 0
	end = start
	max_len = 0
	max_prime = 0
	max_upper = max_lower = 0
	for i in xrange(len(primes) - 1, 0, -1):
		p = primes[i]		
		upper = i - 1		
		lower = upper
		s = primes[upper]	
		while upper > 1:						
			while s < p and lower > 0:
				lower -= 1
				s += primes[lower]		
			if s == p and upper - lower > max_len:
				max_len = upper - lower + 1
				max_prime = p
				max_upper = upper
				max_lower = lower
				upper = lower - 1
				lower = upper
				if upper > 0:
					s = primes[upper]
			else:
				s -= primes[upper]
				upper -= 1
			
	print max_prime
			
if __name__ == '__main__':
	main()
