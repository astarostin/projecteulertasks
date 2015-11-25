import math
import utils


def main():
	print 'Task 52'
	
	for digits in xrange(1, 10):		
		for n in xrange(10 ** (digits - 1), (10 ** digits) / 6):
			if has_same_digits([k*n for k in xrange(1, 7)]):
				print n
				return
					
	
def has_same_digits(numbers):
	lists = []
	for num in numbers:
		lst = [int(x) for x in str(num)]
		lists.append(lst)
	while len(lists) > 1:
		if sorted(lists[0]) == sorted(lists[1]):
			del lists[1]
		else:
			return False
		
	return True
			
if __name__ == '__main__':
	main()
