import utils

limit = 1000000
primes = utils.primes_eratosthenes_bound(limit)
cache = {}
cache2 = {}

def main():
	print 'task 69'
	

	# k = float(limit) / phi(limit)
	# print k

	min_val = 100000
	max_n = 0
	it = 0

	for n in xrange(2, limit):
		it += 1
		# if it % 1000 == 0:
		# 	print it, max_n
		# print n, phi(n)
		k = phi(n)
		if k < min_val:
			min_val = k
			max_n = n
	print max_n


def phi(n):
	if n in primes:
		return (n - 1) / float(n)
	mults = get_prime_factors(n)
	if mults in cache2:
		return cache2[mults]
	res = 1
	for m in mults:
		res *= 1 - 1 / float(m)
	cache2[mults] = res
	return res


def get_prime_factors(n):
	if n in cache:
		return cache[n]
	factors = []
	i = 0
	found = False
	while not found and n > 1 and i < len(primes):
		if n % primes[i] == 0:
			# n /= primes[i]
			factors.append(primes[i])
			factors.extend(get_prime_factors(n / primes[i]))
			found = True
		else:
			i += 1

	res = tuple(sorted(set(factors)))
	cache[n] = res
	return res
	
if __name__ == '__main__':
	main()
