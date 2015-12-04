import utils

def main():
	print 'task 62'
	
	limit = 10000
	data = {}
	code_for_five = None	
	code_for_four = None
	code_for_three = None
	min_five = 10 ** 12
	min_four = 10 ** 12
	min_three = 10 ** 12
	for i in xrange(limit):
		cube = i ** 3
		code = encode(cube)
		if code not in data:
			data[code] = [cube]
		else:
			data[code].append(cube)			
	
	for code in data:
		if len(data[code]) == 5 and min(data[code]) < min_five:
			code_for_five = code
			min_five = min(data[code])
		if len(data[code]) == 4 and min(data[code]) < min_four:
			code_for_four = code
			min_four = min(data[code])
		if len(data[code]) == 3 and min(data[code]) < min_three:
			code_for_three = code	
			min_three = min(data[code])		
	
	
	print min_five	
	
	
def encode(n):
	s = str(n)
	res = [chr(65 + s.count(chr(c))) for c in xrange(48, 58)]
	return ''.join(res)
	
	
if __name__ == '__main__':
	main()