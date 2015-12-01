import utils


def main():
	print 'task 60'
	limit = 1000000
	primes = [str(n) for n in utils.primes_eratosthenes_bound(limit)]
	magic_five_found_so_far = [[3, 31, 4159, 17209, 309571], [3, 31, 3637, 248473, 389401],  [3, 37, 67, 5923, 194119], [3, 37, 607, 276517, 495181], [3, 37, 1699, 208657, 281557], [19, 31, 4723, 221227, 376633]]		
	min_sum_found_so_far = 200149
	sum_min = 1000000
	best_five = None
	fives = get_magic_fives(primes, min_sum_found_so_far)
	print fives
	
	for five in fives:
		s = sum(five)
		if s < sum_min:
			sum_min = s
			best_five = five
			
			
	print best_five
	print sum_min			

	
def get_magic_fives(primes, min_sum_found_so_far):
	threes = set()
	fours = set()
	fives = set()
	pairs = set()
	pairs_map = { }
	for s in primes:
		for i in xrange(1, len(s)):
			if s[i] == '0':
				continue
			s1 = s[:i]
			s2 = s[i:]
			if int(s1) > min_sum_found_so_far or int(s2) > min_sum_found_so_far:
				continue
			if s1 in primes and s2 in primes and s2 + s1 in primes:
				pairs.add((min(int(s1), int(s2)), max(int(s1), int(s2))))				

	for pair in pairs:
		if pair[0] not in pairs_map.keys():
			pairs_map[pair[0]] = set([pair[1]])
		else:
			pairs_map[pair[0]].add(pair[1])
		if pair[1] not in pairs_map.keys():
			pairs_map[pair[1]] = set([pair[0]])
		else:
			pairs_map[pair[1]].add(pair[0])		


	for i in pairs_map.keys():
		for j in pairs_map.keys():
			if i < j and i in pairs_map[j] and j in pairs_map[i]:
				ij = pairs_map[i] & pairs_map[j]
				for k in ij:
					threes.add((i, j, k))				
	
	for p in primes:		
		p = int(p)
		if p > min_sum_found_so_far:
			break
		for three in threes:
			if p not in three:
				combines = True
				for n in three:
					if test_primes(p, n) is not True:
						combines = False
						break
				if combines is True:
					t = list(three)
					t.append(p)
					fours.add(tuple(sorted(t)))	
				
	for p in primes:
		p = int(p)
		if p > min_sum_found_so_far:
			break
		for four in fours:
			if p not in four:
				combines = True
				for n in four:
					if test_primes(p, n) is not True:
						combines = False
						break
				if combines is True:
					t = list(four)
					t.append(p)
					fives.add(tuple(sorted(t)))
	
	return fives

	
def test_primes(p1, p2):
 	s1 = str(p1)
 	s2 = str(p2)
 	return utils.is_prime_simple(int(s1 + s2)) and utils.is_prime_simple(int(s2 + s1))

	
if __name__ == '__main__':
	main()