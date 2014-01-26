import types

def main():
	print 'task 5'
	lim = 20
	print lcm_list(range(2, lim +1))	
	
def gcd(a, b):
	if a == b:
		return a
	if a < b:
		return gcd(b,a)
	if a % b == 0:
		return b
	while rem(a,b) != 0:
		r = rem(a,b)
		a = b
		b = r
	return b

def rem(a, b):
	if a == b:
		return 0
	if a < b:
		rem(b,a)
	if a % b == 0:
		return 0
	i = 1
	while (a - b*i) > b:
		i += 1
	return (a - b*i)

def lcm(a,b):
	return (a*b)//gcd(a,b)

def lcm_list(lst):
	if not type(lst) is types.ListType:
		print 'Not a list given!'
		return 0
 	if len(lst) == 0:
		return 0
	if len(lst) == 1:
		return lst[0]
	if len(lst) == 2:
		return lcm(lst[0], lst[1])
	return lcm(lcm_list(lst[:-1]), lst[-1])

if __name__ == '__main__':
	main()
