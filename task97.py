def main():
	print 'Task 97'

	pwr = 7830457
	res = 1
	for i in range(pwr):
		res *= 2
		if res / 10000000000 > 1:
			res %= 10000000000
	res *= 28433
	res += 1
	print str(res)[-10:]


if __name__ == '__main__':
	main()
