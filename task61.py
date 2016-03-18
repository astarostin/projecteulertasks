import utils

def triangle(n):
	return n * (n + 1) / 2
	
def square(n):
	return n**2
	
def pentagonal(n):
	return n * (3*n - 1) / 2

	
triangles = [triangle(n) for n in xrange(100) if len(str(triangle(n))) == 4]
squares = [square(n) for n in xrange(100) if len(str(square(n))) == 4]
pentagonals = [pentagonal(n) for n in xrange(100) if len(str(pentagonal(n))) == 4]
	
	
def is_magic(n, type):
	if type == 0:
		return n in triangles
	elif type == 1:
		return n in squares
	elif type == 2:
		return n in pentagonals
	return False


def check(n, places):
	for i in xrange(len(places)):
		if places[i] == 0 and is_magic(n, i):
			places[i] = 1
			return i
	return None
	
	
def uncheck(places, i):
	places[i] = 0

def main():
	print 'task 61'
	
	res = []
	places = [0] * 3
	for n1 in xrange(1000, 10000):		
		t1 = check(n1, places)
		if t1 is not None:			
			res.append(n1)				
			if n % 100 > 10:
				start = (n1 % 100) * 100
				for n2 in xrange(start, start + 100):				
					t2 = check(n2, places)
					if t2 is not None:						
						res.append(n2)
						if n % 100 > 10:
							start = (n2 % 100) * 100
							for n3 in xrange(start, start + 100):
								t3 = check(n3, places)
								if t3 is not None:
									res.append(n3)
									print res, n3 % 100, res[0] / 100
									if n3%100 == res[0] / 100:
										print res, sum(res)
									res.pop()
									uncheck(places, t3)
						res.pop()
						uncheck(places, t2)
			res.pop()
			uncheck(places, t1)
		

if __name__ == '__main__':
	main()