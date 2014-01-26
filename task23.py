import math

ab_list = []

def main():
    print 'task 23'   
    data = []
    lim = 28123

    for n in range(1, lim + 1):
        if has_no_abundant_parts(n):
            data.append(n)

    print sum(data)

def has_no_abundant_parts(n):
    i = 1
    res = True
    while i <= n//2:        
        if is_abundant(i) and is_abundant(n - i):
            res = False
            break
        i += 1
        
    return res

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

def is_perfect(n):
    return n == d(n)

def is_deficient(n):
    return d(n) < n

def is_abundant(n):
    if n in ab_list:       
        return True
    if d(n) > n:
        ab_list.append(n)
        return True
    return False

if __name__ == '__main__':
	import timeit
	count=1
	print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)

