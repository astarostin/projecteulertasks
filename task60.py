import utils

limit = 1000
global_primes = utils.primes_eratosthenes_amount(limit)
global_primes_map = utils.numbers_2_batches(utils.primes_eratosthenes_amount(limit * limit))
cache = []

def main():
	print 'task 60'
	
	n = 1000
	k = 5
	z = 2
	
	s = []
	min_sum = 1000000
	while True:
		s = utils.next_selection(limit, k, s)
		selected = [global_primes[i] for i in s]
		cur_sum = check_primes(selected, k, z)
		if cur_sum is not None and cur_sum < min_sum:
			min_sum = cur_sum
			break
		if s is None:
			break
	print min_sum
	
	
def check_primes(primes, k, z):
	s = []
	res = True
	while res:
		s = utils.next_selection(k, z, s)
		if s is None:
			break
		pair = (primes[s[0]], primes[s[1]])
		if pair not in cache:
			if test_primes(primes[s[0]], primes[s[1]]) is not True:
				res = False
			else:
				cache.append(pair)
				
	if res is True:
		return sum(primes)
	else:
		return None
		
	
def test_primes(p1, p2):
	return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))
	
	
def is_prime(n):
	return n in global_primes_map[n / 1000]

if __name__ == '__main__':
	main()
