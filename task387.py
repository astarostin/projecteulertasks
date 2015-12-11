import math
import utils

def main():
	print 'task387'		
	
	res = 0	
	rth_strong_list = generate_strong_harshad(13)	
	for n in rth_strong_list:	
		n *= 10
		for c in [1, 3, 5, 7, 9]:
			num = n + c
			if utils.is_prime_simple(num):
				res += num
	print res			
	

def generate_strong_harshad(limit):
	initial = [x for x in xrange(1, 10)]
	res = []	
	it = 0
	while it < len(initial):
		n = initial[it]
		if len(str(n)) >= limit:
			it +=1
			continue
		s = sum([int(c) for c in str(n)])
		n *= 10
		for c in xrange(0, 10):
			num = n + c
			if num % (s + c) == 0:
				if utils.is_prime_simple(num / (s + c)):					
					res.append(num)
				initial.append(num)
				
		it += 1
	return res	

	
if __name__ == '__main__':
	main()