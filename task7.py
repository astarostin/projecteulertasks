import math

def main():
	print 'task 7'
	n = 10001
	lst=[]
	i = 2
	while len(lst) < n: 
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
	print lst[-1]

if __name__ == '__main__':
	main()
