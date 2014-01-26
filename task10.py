import math

def main():
	print 'task 10'
	n = 2000000
	lst=[]
	i = 2
	while len(lst) == 0 or lst[-1] < n: 
		if i > 10 and (i%2 == 0 or i%5 == 0):
			i += 1
			continue
		is_prime = True   
		sqrt = math.sqrt(i)
		for j in lst:
			if j > sqrt:
				break
			if i % j == 0:
				is_prime = False
				break			
		if is_prime:
			lst.append(i)
		i += 1
	
	print sum(lst[:-1])

if __name__ == '__main__':
	main()
