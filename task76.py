limit = 100
cache = {}
data = [x for x in xrange(limit - 1, 0, -1)]


def main():
	print 'Task 76'
	print solve(max(data) + 1, limit)


def solve(prev, total):
	if (prev, total) in cache:
		return cache[(prev, total)]
	count = 0
	for d in data:
		if d <= prev:
			if d == total:
				count += 1
			if d < total:
				count += solve(d, total - d)
	cache[(prev, total)] = count
	return count


if __name__ == '__main__':
	main()
