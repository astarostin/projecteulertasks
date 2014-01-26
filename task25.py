def main():
    print 'task 25'

    a = 1
    b = 1
    n = 2
    while len(str(b)) < 1000:
        temp = b
        b = a + b
        a = temp
        n += 1

    print b
    print n

if __name__ == '__main__':
	import timeit
	count=1
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)


