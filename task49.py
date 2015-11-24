import math
import utils


def main():
	print 'Task 49'
	upper_limit = 10000
	lower_limit = 1000
	p = utils.primes_eratosthenes_bound(upper_limit)
	q = utils.primes_eratosthenes_bound(lower_limit)
	primes = set(p) - set(q)	
	delta = 3330
	for n in primes:
		if is_prime_and_delta(n + delta, n + 2 * delta, upper_limit, primes) and is_perm(n, n + delta, n + 2 * delta):
			if n != 1487:
				print "%d%d%d" % (n, n + delta, n + 2*delta)	
			

def is_prime_and_delta(b, c, upper_limit, primes):
	return b < upper_limit and b in primes and c < upper_limit and c in primes
			
def is_perm(a, b, c):
	list_a = [int(x) for x in str(a)]
	list_b = [int(x) for x in str(b)]
	list_c = [int(x) for x in str(c)]
		
	return sorted(list_a) == sorted(list_b) and sorted(list_a) == sorted(list_c)
			
if __name__ == '__main__':
	main()
