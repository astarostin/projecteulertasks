def main():
	print 'task 9'
	for a in xrange(1, 500):
		for b in xrange(a, 500):
			c = 1000 - a - b
			if a*a + b*b == c*c:
				print 'a=%d, b=%d, c=%d, abc=%d' % (a, b, c, a*b*c)


if __name__ == '__main__':
	main()
