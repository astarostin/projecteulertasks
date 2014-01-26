def main():
	print 'task 6'
	lim = 100
	#res = trivial(lim)
	res = best(lim)
	print res

def best(n):
	s = n*(n+1) // 2
	sum_sq = (2*n + 1)*(n+1)*n // 6
	return s*s - sum_sq

def trivial(lim):
	s = 0
	for i in xrange(1, lim):
		for j in xrange(i + 1, lim + 1):
			s += i*j
	return s*2


if __name__ == '__main__':
	main()
