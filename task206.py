import re
import math


def main():
	print 'Task 206'

	upper_limit = 1389026623
	lower_limit = 1010101030

	# p = re.compile('1\d2\d3\d4\d5\d6\d7\d8\d900')
	n = lower_limit
	d = 40
	while n < upper_limit:
		sq = str(n * n)
		# if re.match(p, str(n * n)) is not None:
		if sq[0] == '1' and sq[2] == '2' and sq[4] == '3' and sq[6] == '4' and sq[8] == '5' \
			and sq[10] == '6' and sq[12] == '7' and sq[14] == '8':
			print n
			break
		n += d
		d = 100 - d

if __name__ == '__main__':
	main()
