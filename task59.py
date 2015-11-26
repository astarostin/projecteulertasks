import math
import re

def main():
	print 'Task 59'
		
	data = []
	with open('data/task59.txt', 'r') as f:
		for line in f:
			data.extend([int(x) for x in line.strip().split(',')])
	
	(res, text) = decode(data)
	print res
	# print text
	

def decode(data):
	alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
	reg = re.compile('^[a-zA-Z0-9\(\)\-\,\.\+\s\'\;\!\?]+$')
	
	for c1 in alphabet:
		for c2 in alphabet:
			for c3 in alphabet:
				code = c1 + c2 + c3
				key = [ord(c1), ord(c2), ord(c3)]
				decrypted = [data[i] ^ key[i%3] for i in xrange(len(data))]				
				text = ''.join([chr(c) for c in decrypted])				
				m = reg.search(text)
				if m is not None:					
					return (sum(decrypted), text)
			

if __name__ == '__main__':
	main()
