import math


def is_prime_simple(num):
	"""Check if num is prime number.
	:param num: number to check
	"""
	if num < 2:
		return False
	if num == 2:
		return True

	lim = int(math.sqrt(num))
	cur = 2
	while cur <= lim:
		if num % cur == 0:
			return False
		cur += 1

	return True


def primes_eratosthenes_iteration(lst, i):
	""" Perform iteration of eratosthened algorithm
	:param lst: list of primes so far
	:param i: new number to test
	:return: is given number prime or not
	"""
	if i > 10 and (i % 2 == 0 or i % 5 == 0):
		i += 1
		return False
	is_prime = True
	sqrt_val = math.sqrt(i)
	for j in lst:
		if j > sqrt_val:
			break
		if i % j == 0:
			is_prime = False
			break
	return is_prime


def primes_eratosthenes_amount(amount):
	""" Calculates prime numbers using sieve of Eratosthenes method
	:param amount: amount of primes to get
	:return: list of prime numbers
	"""
	lst = []
	i = 2
	while len(lst) < amount:
		if primes_eratosthenes_iteration(lst, i):
			lst.append(i)
		i += 1
	return lst


def primes_eratosthenes_bound(max_value):
	""" Calculates prime numbers using sieve of Eratosthenes method
	:param max_value: max prime value
	:return: list of prime numbers
	"""
	lst = []
	i = 2
	while True:
		if primes_eratosthenes_iteration(lst, i) and i < max_value:
			lst.append(i)
		if i > max_value:
			break
		i += 1
	return lst


def numbers_2_batches(numbers, size=1000):
	""" Organize given list of numbers into batches
	:param numbers:
	:param size:
	:return:
	"""
	res = {}
	for n in numbers:
		batch_id = n / size
		batch = []
		if batch_id not in res:
			res[batch_id] = batch
		else:
			batch = res[batch_id]
		batch.append(n)
	return res


def get_prime_factors(n):
	""" Get a list of all prime factors for given number
	:param n:
	:return:
	"""
	primes = primes_eratosthenes_bound(100000)
	factors = []
	i = 0
	
	while n > 1 and i < len(primes):
		if n % primes[i] == 0:
			n /= primes[i]
			factors.append(primes[i])
		else:
			i += 1

	return factors	


def gcd(a, b):
	"""Calculate GCD for given numbers
	:param a:
	:param b:
	"""
	if a == b:
		return a
	if a < b:
		return gcd(b, a)
	if a % b == 0:
		return b
	while rem(a, b) != 0:
		r = rem(a, b)
		a = b
		b = r
	return b


def lcm(a, b):
	"""Calculate the least common multiplier for given numbers
	:param a:
	:param b:
	"""
	return (a * b) // gcd(a, b)


def lcm_list(lst):
	""" Calculate the least common multiplier for given list
	:param lst: list of numbers
	:return: lcm
	"""
	if len(lst) == 0:
		return 0
	if len(lst) == 1:
		return lst[0]
	if len(lst) == 2:
		return lcm(lst[0], lst[1])
	return lcm(lcm_list(lst[:-1]), lst[-1])


def rem(a, b):
	""" Calculate remainder of division of the given numbers
	:param a:
	:param b:
	:return: remainder
	"""
	if a == b:
		return 0
	if a < b:
		rem(b, a)
	if a % b == 0:
		return 0
	i = 1
	while (a - b * i) > b:
		i += 1
	return a - b * i


def find_all_divisors(n, include_self=True, include_one=True):
	""" Find all divisord for given number
	:param include_one: include 1 to result
	:param include_self: include origin number to result
	:param n: number
	:return: list of divisors
	"""
	lst = []
	i = 1
	j = n // i
	while i < j:
		if n % i == 0:
			lst.append(i)
			j = n // i
			if j != i:
				lst.append(j)
		i += 1
	if not include_self and n in lst:
		lst.remove(n)
	if not include_one:
		lst.remove(1)
	return lst


def fact(n):
	""" Calculate factorial of the given number
	:param n:
	:return: factorial
	"""
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)


def next_perm(data):
	""" Returns next permutation for given list of digits
	:param data: list of digits
	:return:
	"""
	i = len(data) - 1
	while i > 0 and data[i] < data[i - 1]:
		i -= 1
	if i == 0:
		return None
	tail = data[i:]
	before_tail = data[i - 1]
	min_in_tail = 10
	min_in_tail_pos = -1

	for j in range(0, len(tail)):
		if min_in_tail > tail[j] > before_tail:
			min_in_tail = tail[j]
			min_in_tail_pos = j

	if min_in_tail_pos != -1:
		data[i - 1] = min_in_tail
		tail[min_in_tail_pos] = before_tail
		tail.reverse()
		data[i:] = tail

	return data


def is_pandigital(n, lower_bound=1, upper_bound=9):
	""" Check if given number contains all digits from 1 to upper_bound exactly once
	:param n:
	:param lower_bound:
	:param upper_bound:
	:return:
	"""
	if len(str(n)) != upper_bound - lower_bound + 1:
		return False
	for i in xrange(lower_bound, upper_bound + 1):
		if str(i) not in str(n):
			return False
	return True


def count_selections(n, k):
	""" Calculate number of combinatorial selections from n by k
	:param n:
	:param k:
	:return: C from n by k
	"""	
	if k > n - k:
		bigger = k
		smaller = n - k
	else:
		bigger = n - k
		smaller = k
	if bigger == n:
		return 1
	if bigger == n - 1:
		return n
	nom = reduce(lambda x, y: x * y, xrange(bigger + 1, n + 1))
	denom = reduce(lambda x, y: x * y, xrange(1, smaller + 1))
	return nom / denom
	

def measure_time(source, stmt="main()", count=100):
	""" Measure time of given statement
	:param source: source file with statement
	:param stmt: statement to execute and measure
	:param count: count of repeats
	:return: time in seconds
	"""
	import timeit
	print(timeit.timeit(stmt, setup="from " + source + " import " + stmt[:-2], number=count) / count)


def next_selection(n, k, s):
	""" Calculate next selection from n by k for given current selection s
	:param n:
	:param k:
	:param s:
	:return:
	"""
	if len(s) == 0:
		return [x for x in xrange(k)]

	i = k - 1
	j = 1
	while s[i] == n - j and i > 0:
		i -= 1
		j += 1
	if i == 0 and s[i] == n - j:
		return None
	else:
		return s[:i] + [s[i] + 1] + [x for x in xrange(s[i] + 2, s[i] + 2 + k - i - 1)]


def get_selections(n, k):
	""" Calculate all selection from n by k
	:param n:
	:param k:
	:return:
	"""
	res = []
	if k < 1 or k > n:
		return res

	s = []
	while True:
		s = next_selection(n, k, s)
		if s is not None:
			res.append(s)
		else:
			break
	return res
