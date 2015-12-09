import math
import utils

def main():
	print 'task387'	
	
	n = 0
	limit = 10000
	res = 0
	
	for n in xrange(11, limit, 2):
		if is_prime_strong_and_rth(n):
			res += n		
			
	print res			
	
	
def is_harshad(n):
	if n == 0:
		return True
	return n % sum([int(c) for c in str(n)]) == 0
	
	
def is_rth(n):
	if n / 10 == 0:
		return True	
	return is_rth_rec(n / 10)
	

def is_rth_rec(n):
	if n / 10 == 0:
		return is_harshad(n)
	if not is_harshad(n):
		return False
	return is_rth_rec(n / 10)
	
	
def is_strong_harshad(n):
	if n == 0:
		return True
	s = sum([int(c) for c in str(n)])
	return n % s == 0 and utils.is_prime_simple(n / s)
	
def is_prime_strong_and_rth(n):
	if not utils.is_prime_simple(n):
		return False
	if not is_harshad(n / 10):
		return False
	return is_strong_harshad(n / 10) and is_rth(n / 10)

def is_prime(n):
	return n in primes[n / 1000]
	
if __name__ == '__main__':
	main()