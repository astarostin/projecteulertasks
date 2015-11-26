def main():
	print 'task 79'

	data = []
	with open('data/task79.txt', 'rU') as f:
		data = f.readlines()

	print len(data)

if __name__ == '__main__':
	main()
