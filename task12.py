def main():
	print 'task 12'
	num = 1
	step = 2
	divisors = 500

	while find_divisors(num) < divisors:		
		num += step
		step += 1
	print num

def find_divisors(n):
	count = 0
	i = 1
	j = n // i
	while i < j:
		if n % i == 0:			
			count += 1
			j = n // i
			if j != i:
				count +=1
		i += 1
	#print 'num %d, divisors %d' % (n, count)
	return count

if __name__ == '__main__':
	import timeit
	count=1
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)
