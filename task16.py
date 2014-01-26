import sys
import math

def main():

	st = str(2**1000)
	lst = []
	for i in st :
		lst.append(int(i))
	print sum(lst)


if __name__ == '__main__':
	import timeit
	count=1
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)
