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
	return (a*b) // gcd(a, b)


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
	while (a - b*i) > b:
		i += 1
	return a - b * i


def find_all_divisors(n):
	""" Find all divisord for given number
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
	return lst


def is_palindrome(s):
	"""Check string for palindrome
	:param s: string to check
	"""
	return str(s) == str(s)[::-1]


def measure_time(count=100):
	import timeit
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)
