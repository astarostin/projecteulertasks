import math
import utils


def main():
	print 'task 3'
	n = 600851475143
	cur = int(math.sqrt(n))
	found = False
	while not found:
		while cur > 2 and n % cur != 0:
			cur -= 1
		found = utils.is_prime_simple(cur)
		if not found:
			cur -= 1
	
	print cur


if __name__ == '__main__':
	main()
