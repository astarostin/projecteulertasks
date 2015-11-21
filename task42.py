from utils_string import word_value


def main():
	print 'Task 42'
	f = open('data/task42.txt', 'rU')
	data = []
	for line in f:
		data.extend(map(lambda s: s[1:-1], line.split(',')))

	triangles = []
	n = 1
	while len(triangles) < 1000:
		triangles.append(0.5 * n * (n + 1))
		n += 1
	count = 0
	for word in data:
		if word_value(word) in triangles:
			count += 1
	print count

if __name__ == '__main__':
	main()
