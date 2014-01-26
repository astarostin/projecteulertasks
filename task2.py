def main():
	print 'task 2'
	limit = 4000000	
	a, b = 1, 1
	total = a + b
	while a + b <= limit:
		next = a + b
		a = b
		b = next
		if next % 2:
			total = total + next

	print total

if __name__ == '__main__':
	main()
