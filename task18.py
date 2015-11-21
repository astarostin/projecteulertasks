def main():
	print 'task 18'
	f = open('data/task18.txt', 'rU')
	data = []
	for line in f:
		row_str = line.split()
		row = []
		for s in row_str:
			row.append(int(s))
		data.append(row)

	print solve(data)


def solve(data):
	if len(data) == 1:
		return max(data[0])

	row0 = data[0]
	row1 = data[1]
	for i in range(len(row1)):
		elem = row1[i]
		if i == 0:
			elem += row0[0]
		elif i == len(row1) - 1:
			elem += row0[len(row0) - 1]
		else:
			elem += max(row0[i - 1], row0[i])

		row1[i] = elem

	del data[0]
	data[0] = row1
	return solve(data)


if __name__ == '__main__':
	main()
