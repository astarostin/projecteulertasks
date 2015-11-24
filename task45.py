import math


def main():
	print 'Task 45'

	for i in xrange(286, 100000):
		t = trian(i)
		if is_pen(t) and is_hex(t):
			print t
			break
				
	print 'Finished'


def trian(n):
	return n * (n + 1) / 2
	

def is_pen(p):
	return ((1 + math.sqrt(1 + 24 * p)) / 6).is_integer()
	

def is_hex(h):
	return ((1 + math.sqrt(1 + 8 * h)) / 4).is_integer()


if __name__ == '__main__':
	main()
