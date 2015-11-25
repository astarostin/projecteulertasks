import math
import utils


def main():
	print 'Task 53'
	
	total = 0
	limit = 1000000
	for n in xrange(1, 101):
		for k in xrange(1, n + 1):
			if utils.count_selections(n, k) > limit:
				total += 1
	print total
	
			
if __name__ == '__main__':
	main()
