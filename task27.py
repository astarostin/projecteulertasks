import math

primes = []
squares = {}
#ANSWER: max_a = -61 max_b = 971, a*b = -59231

def main():
    print 'task 27'
    lim = 1000
    #eratosphen(1000000)
    fill_primes(100000)
    fill_squares(100)
    
    max_prime = 0
    max_a = 0
    max_b = 0    
    for a in range(-lim+1, lim, 1):
        for b in range(2, lim, 1):
            if b in primes:
                primes_n = test(a,b)
                if primes_n > max_prime:
                    max_prime = primes_n
                    max_a = a
                    max_b = b
    print 'max_a = %d max_b = %d, a*b = %d, max_prime = %d' % (max_a, max_b, max_a*max_b, max_prime)

def fill_squares(lim):
    for i in range(lim+1):
        squares[i] = i*i

def eratosphen(lim):
    for i in range(2, lim+1):
        primes.append(i)
    
    was_deletions = True
    i = 0
    while i < len(primes):
        a = primes[i]
        for n in primes:
            if n > a and n%a == 0:
                primes.remove(n)
        i += 1

def test(a,b):
    n = 0
    prime = True    
    while prime:
        num = squares[n] + a*n + b
        if num in primes:
            n += 1
        else:
            prime = False
            
    return n

def fill_primes(lim):    
    for i in range(2, lim):
        if is_prime(i):
            primes.append(i)

def is_prime(n):    
    i = 2
    while i <= math.sqrt(n):
        if n%i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    main()
