import utils
import math

limit = 100000000
primes = utils.numbers_2_batches(utils.primes_eratosthenes_bound(limit))


def main():
	print 'task357'
	n = 2
	res = 3
	
	cache_true = []	
	prev_acceptable = False
	
	while n < limit:
		n += 1
		d = 1
		if n % 100000 == 0:
			print n, res
		
		#if prev_acceptable:			
		#	prev_acceptable = False
		#	continue
		#else: 		
		#cur_prime = is_prime(n)
		
		if prev_acceptable or is_prime(n):			
			prev_acceptable	= False
			continue
		
		acceptable = True
	
		while d <= math.sqrt(n):
			if n % d == 0:
				p = d + n / d								
				if not is_prime(p):									
					acceptable = False								
					break	
			d += 1		
		if not acceptable:
			prev_acceptable = False
			continue
		res += n
		prev_acceptable = True
	
	print res
	

def is_prime(n):
	return n in primes[n / 1000]
	
if __name__ == '__main__':
	main()