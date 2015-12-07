import utils
from numpy import loadtxt

def main():
	print 'task 81'
	m = loadtxt('data/task81.txt', dtype='int', delimiter=',')
	print m[1][3]
	
if __name__ == '__main__':
	main()