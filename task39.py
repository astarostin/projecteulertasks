import math


def main():
	print 'Task 39'
	perimeters = {}
	for x in xrange(1, 1000):
		for y in xrange(x, 1000):
			per = x + y + math.sqrt(x**2 + y**2)
			if per > 1000:
				continue
			if per not in perimeters:
				perimeters[per] = 1
			else:
				perimeters[per] += 1
	max_count = 0
	res = 0
	for p in perimeters:
		if perimeters[p] > max_count:
			max_count = perimeters[p]
			res = p
	print res


if __name__ == '__main__':
	main()
