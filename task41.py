import utils


def main():
	print 'Task 41'
	data = [1, 2]
	max_prime = 0
	while len(data) < 9:
		data.append(len(data) + 1)
		start_perm = data[:]
		max_prime = check_prime_and_max(data, max_prime)
		data = utils.next_perm(data)
		while data is not None:
			max_prime = check_prime_and_max(data, max_prime)
			data = utils.next_perm(data)
		data = start_perm[:]
	print max_prime


def check_prime_and_max(data, max_prime):
	n = int(reduce(lambda x, y: str(x) + str(y), data))
	if utils.is_prime_simple(n) and n > max_prime:
		return n
	return max_prime

if __name__ == '__main__':
	main()
