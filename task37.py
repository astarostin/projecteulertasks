import utils

primes = utils.primes_eratosthenes_amount(100000)
cache_left_to_right = []
cache_right_to_left = []


def main():
	print 'Task 37'
	s = 0
	cnt = 0
	for n in primes:
		if n > 7 and is_truncable_prime(str(n)):
			cnt += 1
			s += n
			if cnt == 11:
				break
	if cnt < 11:
		print 'Not enough primes: ' + str(cnt)
	else:
		print s


def is_truncable_prime_left_to_right(s):
	if int(s) not in primes:
		return False
	if len(s) == 1:
		return True
	if int(s) in cache_left_to_right:
		return True
	res = is_truncable_prime_left_to_right(s[1:])
	if res is True and res not in cache_left_to_right:
		cache_left_to_right.append(int(s))
	return res


def is_truncable_prime_right_to_left(s):
	if int(s) not in primes:
		return False
	if len(s) == 1:
		return True
	if int(s) in cache_right_to_left:
		return True
	res = is_truncable_prime_right_to_left(s[:-1])
	if res is True and res not in cache_right_to_left:
		cache_right_to_left.append(int(s))
	return res


def is_truncable_prime(s):
	return is_truncable_prime_left_to_right(s[1:]) and is_truncable_prime_right_to_left(s[:-1])


if __name__ == '__main__':
	main()
