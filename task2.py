def main():
	print 'task 2'
	limit = 4000000	
	a, b = 1, 1
	total = a + b
	while a + b <= limit:
		next_value = a + b
		a = b
		b = next_value
		if next_value % 2:
			total += next_value

	print total

if __name__ == '__main__':
	main()
