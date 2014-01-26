import math

def main():
    print 'task 21'
    lim = 10000
    data = []

    for n in range(1, lim):
        if not n in data:
            dn = d(n)
            if n == d(dn) and n != dn:
                data.append(n)                
                data.append(dn)    
    print sum(data)    
    
def d(n):
    if n == 1:
        return 1
    divs = [1]

    i = 2
    lim = math.sqrt(n)
    while i <= lim:
        if n%i == 0:
            divs.append(i)
            if i*i != n:
                divs.append(n // i)
        i += 1
    
    return sum(divs)

if __name__ == '__main__':
	import timeit
	count=1
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)

