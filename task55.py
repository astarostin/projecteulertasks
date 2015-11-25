import math
import utils
import utils_string


def main():
	print 'Task 55'
	
	total = 0
	max_iter = 50
	for n in xrange(1, 10000):
		iter = 1
		palindrome = False
		num = n
		while not palindrome and iter < max_iter:
			num = next(num)
			palindrome = utils_string.is_palindrome(num)
			iter += 1
		if not palindrome:
			total += 1			
	print total
	

def next(n):
	return n + int(str(n)[::-1])
	
			
if __name__ == '__main__':
	main()
