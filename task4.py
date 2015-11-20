import utils


def main():
	print 'task 4'
	n = 0
	for i in range(999, 99, -1):
		for j in range(999, i - 1, -1):
			if i*j < n:
				break
			if utils.is_palindrome(i*j) and i*j > n:
				n = i*j
	print n


if __name__ == '__main__':
	main()
