import math
import utils

def main():
	print 'task387'	
	
	n = 0
	limit = 1000000
	res = 0
	start = 11
	s = 9
	
	for n in xrange(start, limit, 2):
		if n % 10000 == 1:
			s = sum([int(c) for c in str(n)])
		elif n % 1000 == 1:
			s -= 25
		elif n % 100 == 1:
			s -= 16
		elif n % 10 == 1:
			s -= 7			
		else:
			s += 2
		if is_prime_strong_and_rth(n, s):
			res += n		
			
	print res			
	
	
def is_harshad(n, s):
	if n == 0:
		return True
	return n % s == 0
	
	
def is_rth(n, s):
	if n / 10 == 0:
		return True	
	s -= n % 10
	return is_rth_rec(n / 10, s)
	

def is_rth_rec(n, s):
	if n / 10 == 0:
		return is_harshad(n, s)
	if not is_harshad(n, s):
		return False
	s -= n % 10
	return is_rth_rec(n / 10, s)
	
	
def is_strong_harshad(n, s):
	if n == 0:
		return True	
	return n % s == 0 and utils.is_prime_simple(n / s)
	
def is_prime_strong_and_rth(n, s):
	if not utils.is_prime_simple(n):
		return False
	s -= n % 10
	if not is_harshad(n / 10, s):
		return False
	return is_strong_harshad(n / 10, s) and is_rth(n / 10, s)

def is_prime(n):
	return n in primes[n / 1000]
	
if __name__ == '__main__':
	main()