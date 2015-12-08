import utils
from numpy import loadtxt
import sys

def main():
	print 'task 81'
	m = loadtxt('data/task81.txt', dtype='int', delimiter=',')
	h = m.shape[0]
	w = m.shape[1]
	print h, w
	for i in xrange(h - 1, -1, -1):
		for j in xrange(w - 1, -1, -1):			
			if i == h - 1 and j == w - 1:
				continue
			right = sys.maxint
			if j < w - 1:
				right = m[i][j + 1]
			down = sys.maxint
			if i < h - 1:
				down = m[i + 1][j]
			m[i][j] += min(right, down)
	print m[0][0]
	
if __name__ == '__main__':
	main()