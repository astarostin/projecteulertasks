import math
import utils
import utils_string


def main():
	print 'Task 58'
		
	limit = 1000000
	# primes = utils.primes_eratosthenes_bound(limit)
	border = 0.1
	num_primes = 0
	total = 1
	for n in xrange(3, limit, 2):	
		num_primes += get_new_diag_primes_count(n)
		total += 4		
		if float(num_primes) / total < border:
			print n
			break
	

def get_new_diag_primes_count(n):
	s1 = (n - 2) ** 2
	s2 = n - 1
	elems = [s1 + i * s2 for i in range(1, 5)]		
	return len([x for x in elems if utils.is_prime_simple(x)])
	
			
if __name__ == '__main__':
	main()
