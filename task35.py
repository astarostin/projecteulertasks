import math

primes = []


def main():
	print 'task 35'
	fill_primes()
	res = 0
	for p in primes:
		if test(p):
			res += 1
	print res


def test(n):
	n = rotate(n)
	i = 1
	while i < len(str(n)):

		if n not in primes:
			return False
		n = rotate(n)
		i += 1
	return True


def rotate(n):
	s = str(n)
	if len(s) == 1:
		return n
	return int(s[-1] + s[:-1])


def fill_primes():
	lim = 1000000
	for i in range(2, lim):
		if is_prime(i):
			primes.append(i)


def is_prime(n):
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i += 1

	return True


if __name__ == '__main__':
	main()
