def main():
	print 'task 79'

	with open('data/task79.txt', 'rU') as f:
		data = [s.strip() for s in f.readlines()]

	data = list(set(data))
	# data.append('187')
	m = [[0 for i in range(10)] for j in range(10)]
	for d in data:
		for i in range(len(d) - 1):
			for j in range(i + 1, len(d)):
				m[int(d[i])][int(d[j])] = 1

	# for index, row in enumerate(m):
	# 	print index, row

	numbers = [x for x in range(10) if sum(m[x]) > 0 or sum([m[i][x] for i in range(10)]) > 0]

	result = []
	for x in numbers:
		k = len(result)
		while k > 0 and compare(x, result[k - 1], m) == -1:
			k -= 1
		# if k > 0 and compare(x, result[k - 1], m) == 2:
		# 	if x not in result[:k]:
		# 		result.insert(k, x)
		# 	k -= 1
		# 	while k > 0 and compare(x, result[k - 1], m) == -1:
		# 		k -= 1
		# 	result.insert(k, x)
		# else:
		result.insert(k, x)

	print ''.join([str(c) for c in result])


def compare(a, b, m):
	if m[a][b] == 0 and m[b][a] == 0:
		return 0
	if m[a][b] == 1 and m[b][a] == 0:
		return -1
	if m[a][b] == 0 and m[b][a] == 1:
		return 1
	return 2


if __name__ == '__main__':
	main()
