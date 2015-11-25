import math
import utils
import utils_string


def main():
	print 'Task 56'
		
	max_sum = 50
	for a in xrange(1, 100):
		for b in xrange(1, 100):
			s = digit_sum(a ** b)
			if s > max_sum:
				max_sum = s
	print max_sum		
	

def digit_sum(n):
	return sum([int(c) for c in str(n)])
	
			
if __name__ == '__main__':
	main()
