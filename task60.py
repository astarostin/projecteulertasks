import utils


# k = 5
# z = 2
# batch_size = 100

# global_primes_map = utils.numbers_2_batches(utils.primes_eratosthenes_amount(limit * limit), sz=batch_size)
# sel_indices_from_5_by_2 = utils.get_selections(k, z)
# cache_true = []
# cache_false = []

def main():
	print 'task 60'
	limit = 1000000
	# counts = {str(i): 0 for i in xrange(limit)}
	pairs = set()
	primes = [str(n) for n in utils.primes_eratosthenes_bound(limit)]
	pairs_map = { }
	for s in primes:
		for i in xrange(1, len(s)):
			if s[i] == '0':
				continue
			s1 = s[:i]
			s2 = s[i:]
			if s1 in primes and s2 in primes and s2 + s1 in primes:
				pairs.add((min(int(s1), int(s2)), max(int(s1), int(s2))))
				# counts[s1] += 1
				# counts[s2] += 1

	for pair in pairs:
		if pair[0] not in pairs_map.keys():
			pairs_map[pair[0]] = set([pair[1]])
		else:
			pairs_map[pair[0]].add(pair[1])
		if pair[1] not in pairs_map.keys():
			pairs_map[pair[1]] = set([pair[0]])
		else:
			pairs_map[pair[1]].add(pair[0])
		#print pairs_map[pair[0]]

	#print pairs_map

	for i in pairs_map.keys():
		for j in pairs_map.keys():
			if i < j and i in pairs_map[j] and j in pairs_map[i]:
				ij = pairs_map[i] & pairs_map[j]
				if len(ij) > 0:
					for k in pairs_map.keys():
						if j < k and i in pairs_map[k] and j in pairs_map[k] and k in pairs_map[i] and k in pairs_map[j]:
							ijk = ij & pairs_map[k]
							if len(ijk) > 0:
								print i, j, k, ijk

	# for key, value in counts.items():
	# 	if value > 10:
	# 		print '%s - %s times' % (key, value)


# def main():
# 	print 'task 60'
#
# 	s = []
# 	min_sum = 1000000
#
# 	while True:
# 		s = utils.next_selection(limit, k, s)
# 		if s is None:
# 			break
# 		selected = [global_primes[i] for i in s]
# 		if sum(selected) > 1000:
# 			continue
# 		cur_sum = check_primes(selected)
# 		if cur_sum is not None and cur_sum < min_sum:
# 			min_sum = cur_sum
# 			break
#
# 	print min_sum
#
#
# def check_primes(primes):
# 	res = True
# 	for s in sel_indices_from_5_by_2:
# 		pair = (primes[s[0]], primes[s[1]])
# 		if pair in cache_false:
# 			res = False
# 			break
# 		elif pair not in cache_true:
# 			if test_primes(primes[s[0]], primes[s[1]]) is not True:
# 				cache_false.append(pair)
# 				res = False
# 				break
# 			else:
# 				cache_true.append(pair)
#
# 	if res is True:
# 		return sum(primes)
# 	else:
# 		return None
#
#
# def test_primes(p1, p2):
# 	s1 = str(p1)
# 	s2 = str(p2)
# 	return is_prime(int(s1 + s2)) and is_prime(int(s2 + s1))
#
#
# def is_prime(n):
# 	return utils.is_prime_simple(n)
	# return n in global_primes_map[n / batch_size]

if __name__ == '__main__':
	main()


# '''
# 3 7 109 set([673])
# 3 7 673 set([109])
# 3 37 67 set([2377, 5923])
# 3 37 2377 set([67])
# 3 37 5923 set([67])
# 3 67 2377 set([37])
# 3 67 5923 set([37])
# 3 109 673 set([7])
# 7 19 97 set([4507, 3727])
# 7 19 3727 set([97])
# 7 19 4507 set([97])
# 7 97 3727 set([19])
# 7 97 4507 set([19])
# 7 109 673 set([3])
# 19 97 3727 set([7])
# 19 97 4507 set([7])
# 23 677 827 set([311])
# 23 311 677 set([827])
# 23 311 827 set([677])
# 37 67 2377 set([3])
# 37 67 5923 set([3])
# 311 677 827 set([23])
# '''