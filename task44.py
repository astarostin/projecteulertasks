import math


def main():
	print 'Task 44'
	min_d = 100000000

	cache = {n: pen(n) for n in xrange(1, 3000)}
	for i in xrange(1, len(cache.keys()) - 1):
		p_i = cache[i]
		for j in xrange(i + 1, len(cache.keys())):
			# print 'j = %d' % j
			p_j = cache[j]
			s = p_i + p_j
			d = int(math.fabs(p_i - p_j))
			if rev(s) and rev(d):
				# print "Found: %d(%d) - %d(%d)" % (i, p_i, j, p_j)
				if d < min_d:
					min_d = d
	print min_d


def rev(p):
	return ((1 + math.sqrt(1 + 24 * p)) / 6).is_integer()


def pen(n):
	return n * (3 * n - 1) / 2

if __name__ == '__main__':
	main()
