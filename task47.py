import math
import utils


primes = utils.primes_eratosthenes_bound(100000)


def main():
	print 'Task 47'

	start_num = 3
	chain_len = 4
	cur_list = [x for x in range (start_num, start_num + chain_len)]		
	cur_list_primes_num = [get_distinct_factors_num(x) for x in cur_list]	
	found = False
	next_num = start_num + chain_len
	while not (len(set(cur_list_primes_num)) == 1 and cur_list_primes_num[0] == chain_len):
		del cur_list[0]
		cur_list.append(next_num)
		del cur_list_primes_num[0]
		cur_list_primes_num.append(get_distinct_factors_num(next_num))
		next_num += 1					
				
	print cur_list[0]


def get_prime_factors(n):
	factors = []
	i = 0;
	
	while n > 1 and i < len(primes):
		if n % primes[i] == 0:
			n /= primes[i]
			factors.append(primes[i])
		else:
			i += 1

	return factors
	
	
def get_distinct_factors_num(n):
	return len(set(get_prime_factors(n)))

if __name__ == '__main__':
	main()
