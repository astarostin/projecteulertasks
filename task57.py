import math
import utils
import utils_string


def main():
	print 'Task 57'
		
	limit = 1000
	total = 0
	n, d = 3, 2
	for i in xrange(2, limit):	
		(n, d) = next(n, d)
		if len(str(n)) > len(str(d)):
			total += 1
	print total
	

def next(n, d):
	return (n + 2 * d, n + d)
	
			
if __name__ == '__main__':
	main()
