import math

def main():
	print 'task 3'
	n = 600851475143
	factor = 0
	cur = int(math.sqrt(n))
	found = False
	while not found:
		while cur > 2 and n % cur != 0:			
			cur = cur - 1
		found = is_prime(cur)
		if not found:
			cur = cur - 1
	
	print cur

def is_prime(num):
	print 'Testing %d' % num
	if num < 2:
		return False
	if num == 2:
		return True

	lim = int(math.sqrt(num))
	cur = 2
	while cur <= lim:
		if num % cur == 0:
			return False		
		cur = cur + 1
	
	return True

if __name__ == '__main__':
	main()
