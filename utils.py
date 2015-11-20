import math


def is_prime(num):
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


def is_palindrome(s):
	"""Check string for palindrome
	:param s: string to check
	"""
	return str(s) == str(s)[::-1]
