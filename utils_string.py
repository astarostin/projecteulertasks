NUMBERS_NAMES = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
				 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
				 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
				 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'one thousand'}


def num2str(num):
	""" Convert number to text representation
	:param num: number to convert
	:return: text representation
	"""
	if num in NUMBERS_NAMES:
		if num == 100:
			return 'one ' + NUMBERS_NAMES[num]
		return NUMBERS_NAMES[num]
	res = ''
	if num > 100:
		res += NUMBERS_NAMES[int(num // 100)] + ' ' + NUMBERS_NAMES[100]
		tail = num % 100
		if tail != 0:
			res += ' and '
			if tail in NUMBERS_NAMES:
				res += NUMBERS_NAMES[tail]
			else:
				res += NUMBERS_NAMES[tail - tail % 10] + ' ' + NUMBERS_NAMES[tail % 10]
	else:
		res += NUMBERS_NAMES[int(num - num % 10)] + ' ' + NUMBERS_NAMES[num % 10]
	return res


def is_palindrome(s):
	"""Check string for palindrome
	:param s: string to check
	"""
	return str(s) == str(s)[::-1]


def word_value(s):
    res = 0
    for c in s:
        res += (ord(c) - ord('A') + 1)

    return res