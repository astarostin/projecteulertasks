# digits = {str(n): 0 for n in xrange(10)}
digits2 = {str(n): [0, 0, 0] for n in xrange(10)}
m = [[0 for i in range(10)] for j in range(10)]
def main():
	print 'task 79'

	pswd = []

	with open('data/task79.txt', 'rU') as f:
		data = [s.strip() for s in f.readlines()]

	data = list(set(data))
	
		
	for d in data:
		for i in range(len(d) - 1):
			m[int(d[i])][int(d[i + 1])] += 1
			# digits[d[i]] += 1
			# digits2[d[i]][i] += 1
			
	for index, row in enumerate(m):
		print index, row, sum(row)	

	# freq = [(d, digits[d]) for d in sorted(digits.keys(), cmp=lambda a, b: digits[b] - digits[a])]
	# freq2 = [(d, digits2[d]) for d in sorted(digits2.keys(), cmp=srt2)]
	# print freq
	# print freq2
	data.sort(cmp=srt3)	
	print data
	numbers = [x for x in range(10)]
	numbers.sort(cmp=srt4)
	print numbers


# def srt(a, b):
# 	differs_at = 0
# 	while differs_at < min(len(a), len(b)) and a[differs_at] == b[differs_at]:
# 		differs_at += 1
# 	if differs_at == min(len(a), len(b)):
# 		return 0
# 	if digits[a[differs_at]] > digits[b[differs_at]]:
# 		return -1
# 	else:
# 		return 1


def srt2(a, b):
	if digits2[a][0] > digits2[b][0]:
		return -1
	elif digits2[a][0] < digits2[b][0]:
		return 1

	if digits2[a][1] > digits2[b][1]:
		return 1
	elif digits2[a][1] < digits2[b][1]:
		return -1

	if digits2[a][2] > digits2[b][2]:
		return -1
	elif digits2[a][2] < digits2[b][2]:
		return 1
	else:
		return 0
		
def srt3(a, b):
	differs_at = 0
 	while differs_at < min(len(a), len(b)) and a[differs_at] == b[differs_at]:
 		differs_at += 1
 	if differs_at == min(len(a), len(b)):
 		return 0
 	if m[int(a[differs_at])][int(b[differs_at])] > m[int(b[differs_at])][int(a[differs_at])]:
 		return -1
 	else:
 		return 1
	
	
def srt4(a, b):		
	if a == b or m[a][b] == m[b][a]:		
 		return 0
 	if m[a][b] > m[b][a]:				
 		return -1
 	else:				
 		return 1

if __name__ == '__main__':
	main()
