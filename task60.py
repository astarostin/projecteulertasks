import utils

limit = 1000000
TEN_POWERS = {1: 10, 2: 100, 3: 1000, 4: 10000, 5: 100000, 6: 1000000}
primes3 = set(utils.primes_eratosthenes_bound(limit))
cache_true = set()
cache_true_pair = set()
# cache_false = set()
# cache_false_pair = set()

def main():
	print 'task 60'

	min_sum_found_so_far = 76721
	#primes = [str(n) for n in utils.primes_eratosthenes_bound(limit)]
	primes2 = utils.primes_eratosthenes_bound(min_sum_found_so_far + 1)

	magic_five_found_so_far = [[3, 31, 4159, 17209, 309571], [3, 31, 3637, 248473, 389401],
							   [3, 37, 67, 5923, 194119], [3, 37, 607, 276517, 495181], [3, 37, 1699, 208657, 281557],
							   [19, 31, 4723, 221227, 376633], [7, 19, 8941, 51133, 171533],
							   [733, 883, 991, 18493, 55621]]
	# (733, 883, 991, 18493, 55621)	
	f = open('data/task60_fives_known.txt', 'w')
	for five in magic_five_found_so_far:
		f.write(' '.join([str(c) for c in five]) + '\n')
	f.close()
	sum_min = 1000000
	best_five = None
	fives = get_magic_fives(primes2, min_sum_found_so_far)	
	
	for five in fives:
		s = sum(five)
		if s < sum_min:
			sum_min = s
			best_five = five

	print best_five
	print sum_min			

	
def get_magic_fives(primes2, min_sum_found_so_far):
	threes = set()
	fours = set()
	fives = set()
	# pairs = set()
	pairs_map = {}
	# for s in primes:
	# 	for i in xrange(1, len(s)):
	# 		if s[i] == '0':
	# 			continue
	# 		s1 = s[:i]
	# 		s2 = s[i:]
	# 		if int(s1) > min_sum_found_so_far or int(s2) > min_sum_found_so_far:
	# 			continue
	# 		if s1 in primes and s2 in primes and s2 + s1 in primes:
	# 			pairs.add((min(int(s1), int(s2)), max(int(s1), int(s2))))

	it = 0
	for i in xrange(len(primes2) - 1):
		n1 = primes2[i]
		if it > 4000000:
			break
		for j in xrange(i + 1, len(primes2)):
			it += 1
			if it % 100000 == 0:				
				print it, len(pairs_map.keys()), len(cache_true)# , len(cache_false)			
				cache_true.clear()			
				
			n2 = primes2[j]
			#if (str(n1) + str(n2)) in primes3 and (str(n2) + str(n1)) in primes3:
			if test_primes(n1, n2):
				if n1 not in pairs_map:
					pairs_map[n1] = {n2}
				else:
					pairs_map[n1].add(n2)
				if n2 not in pairs_map:
					pairs_map[n2] = {n1}
				else:
					pairs_map[n2].add(n1)
	cache_true.clear()

	# print 'Got pairs'
	#
	# for pair in pairs:
	# 	if pair[0] not in pairs_map.keys():
	# 		pairs_map[pair[0]] = {pair[1]}
	# 	else:
	# 		pairs_map[pair[0]].add(pair[1])
	# 	if pair[1] not in pairs_map.keys():
	# 		pairs_map[pair[1]] = {pair[0]}
	# 	else:
	# 		pairs_map[pair[1]].add(pair[0])
			
	print 'Got pairs_map', len(pairs_map.keys())

	for i in pairs_map:
		for j in pairs_map:
			if i < j and i in pairs_map[j] and j in pairs_map[i]:
				ij = pairs_map[i] & pairs_map[j]
				for k in ij:
					if i + j + k < min_sum_found_so_far:
						threes.add((i, j, k))				

	print 'Got threes'
	f = open('data/task60_threes.txt', 'w')
	for three in threes:
		f.write(' '.join([str(c) for c in three]) + '\n')
	f.close()
	
	for p in primes2:				
		for three in threes:
			if p not in three and sum(three) + p < min_sum_found_so_far: 
				combines = True
				for n in three:
					if test_primes(p, n) is not True:
						combines = False
						break
				if combines is True:
					t = list(three)
					t.append(p)
					fours.add(tuple(sorted(t)))	
	
	print 'Got fours'
	f = open('data/task60_fours.txt', 'w')
	for four in fours:
		f.write(' '.join([str(c) for c in four]) + '\n')
	f.close()
				
	for p in primes2:				
		for four in fours:
			if p not in four and sum(four) + p < min_sum_found_so_far:
				combines = True
				for n in four:
					if test_primes(p, n) is not True:
						combines = False
						break
				if combines is True:
					t = list(four)
					t.append(p)
					fives.add(tuple(sorted(t)))
	print 'Got fives'
	f = open('data/task60_fives.txt', 'w')
	for five in fives:
		f.write(' '.join([str(c) for c in five]) + '\n')
	f.close()
	
	return fives

	
# def test_primes(p1, p2):
# 	s1 = str(p1)
# 	s2 = str(p2)
# 	return utils.is_prime_simple(int(s1 + s2)) and utils.is_prime_simple(int(s2 + s1))


def test_primes(n1, n2):
	# pair = (min(n1, n2), max(n1, n2))
	# if pair in cache_true_pair:
	# 	print 'Hit pair true'
	# 	return True
	# if pair in cache_false_pair:
	# 	print 'Hit pair false'
	# 	return False
	c1, c2 = int(str(n1) + str(n2)), int(str(n2) + str(n1)) #concat(n1, n2)
	res = is_prime(c1) and is_prime(c2)
	# if res is True:
	# 	cache_true_pair.add(pair)
	# else:
	# 	cache_false_pair.add(pair)
	return res
	#return utils.is_prime_simple(c1) and utils.is_prime_simple(c2)
	#return c1 in primes3 and c2 in primes3


def is_prime(n):
	if n in primes3:
		return True
	if n in cache_true:
		return True
	# elif n in cache_false:
	# 	return False
	else:
		if utils.is_prime_simple(n):
			cache_true.add(n)
			return True
		else:
			# cache_false.add(n)
			return False


def concat(n1, n2):
	# return int(str(n1) + str(n2)), int(str(n2) + str(n1))
	len1 = get_len(n1)
	len2 = get_len(n2)
	return n1 * TEN_POWERS[len2] + n2, n2 * TEN_POWERS[len1] + n1


def get_len(n):
	res = 0
	while n > 0:
		n /= 10
		res += 1
	return res

if __name__ == '__main__':
	main()