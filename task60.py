import utils

limit = 10000
primes = utils.primes_eratosthenes_bound(limit)
cache_true = set()

def main():
	print 'task 60'
	
	result = 50000
	pairs_list = [None for i in primes]
	for a in xrange(1, len(primes)):
		if primes[a] * 5 > result:
			break
		if pairs_list[a] is None:
			pairs_list[a] = make_pair(a)
		for b in xrange(a + 1, len(primes)):
			if primes[a] + 4 * primes[b] > result:
				break
			if primes[b] not in pairs_list[a]:
				continue
			if pairs_list[b] is None:
				pairs_list[b] = make_pair(b)
			for c in xrange(b + 1, len(primes)):
				if primes[a] + primes[b] + 3 * primes[c] > result:
					break
				if primes[c] not in pairs_list[a] or primes[c] not in pairs_list[b]:
					continue
				if pairs_list[c] is None:
					pairs_list[c] = make_pair(c) 
				for d in xrange(c + 1, len(primes)):
					if primes[a] + primes[b] + primes[c] + 2 * primes[d] > result:
						break
					if primes[d] not in pairs_list[a] or primes[d] not in pairs_list[b] or primes[d] not in pairs_list[c]:
						continue
					if pairs_list[d] is None:
						pairs_list[d] = make_pair(d)
					for e in xrange(d + 1, len(primes)):
						if primes[a] + primes[b] + primes[c] + primes[d] + primes[e] > result:
							break
						if primes[e] not in pairs_list[a] or primes[e] not in pairs_list[b] or primes[e] not in pairs_list[c] or primes[e] not in pairs_list[d]:
							continue
						if pairs_list[e] is None:
							pairs_list[e] = make_pair(e)
						if primes[a] + primes[b] + primes[c] + primes[d] + primes[e] < result:
							result = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
						# print 'Five found: %d %d %d %d %d' % (primes[a], primes[b], primes[c], primes[d], primes[e])
	print result
			
def make_pair(i):
	pairs = set()
	a = primes[i]
	for j in xrange(i + 1, len(primes)):
		b = primes[j]
		c1, c2 = concat(a, b)
		if is_prime(c1) and is_prime(c2):
			pairs.add(b)
	return pairs
	
def is_prime(n):	
	if n in primes:
		return True
	if n in cache_true:
		return True	
	else:
		if utils.is_prime_simple(n):
			cache_true.add(n)
			return True
		else:		
			return False


def concat(n1, n2):
	return int(str(n1) + str(n2)), int(str(n2) + str(n1))	

	
if __name__ == '__main__':
	main()