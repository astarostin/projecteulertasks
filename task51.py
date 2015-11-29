from utils import is_prime_simple
from utils import get_selections


cache_selections = {}


def main():
	print 'Task 51'
	max_primes = 8
	digits_amount = 6
	lower_bound = 100001
	upper_bound = 999999

	for n in xrange(lower_bound, upper_bound, 2):
		list_chars = list(str(n))
		for i in xrange(1, digits_amount):
			if (digits_amount - 1, i) in cache_selections:
				subs = cache_selections[(digits_amount - 1, i)]
			else:
				subs = get_selections(digits_amount - 1, i)
				cache_selections[(digits_amount - 1, i)] = subs

			for sub in subs:
				primes = []

				for value in substitutions(list_chars[:], sub):
					if is_prime_simple(int(value)):
						primes.append(value)
				if len(primes) == max_primes:
					print int(primes[0])
					return


def substitutions(list_chars, sub):
	res = []
	if 0 in sub:
		first_k = 1
	else:
		first_k = 0
	for k in xrange(first_k, 10):
		s = str(k)
		for p in sub:
			list_chars[p] = s
		res.append(''.join(list_chars))
	return res


if __name__ == '__main__':
	main()
