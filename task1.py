def main():
	print 'task 1'
	n = 1000
	s = 0
	for i in range(n):
		if i % 3 == 0 or i % 5 == 0:
			s += i
	print s

if __name__ == '__main__':
	main()
