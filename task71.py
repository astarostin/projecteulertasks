import utils


def main():
	print 'Task 71'

	closest = 2.0 / 5
	value = 3.0 / 7
	min_dist = value - closest
	min_dist_nom = 0
	for d in xrange(9, 1000001):
		if d % 100000 == 0:
			print d, min_dist_nom
		nom = int(d * value)
		cur_dist = value - float(nom) / d
		if cur_dist > min_dist:
			continue
		while utils.gcd(nom, d) != 1:
			nom -= 1
		cur_dist = value - float(nom) / d
		if cur_dist < min_dist:
			min_dist = cur_dist
			min_dist_nom = nom
	print min_dist_nom

if __name__ == '__main__':
	main()
