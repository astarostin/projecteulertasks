import utils


def main():
    print 'task 27'
    lim = 1000
    primes = utils.primes_eratosthenes_bound(100000)
    squares = fill_squares(100)
    
    max_prime = 0
    max_a = 0
    max_b = 0    
    for a in range(-lim + 1, lim, 1):
        for b in range(2, lim, 1):
            if b in primes:
                primes_n = test(a, b, primes, squares)
                if primes_n > max_prime:
                    max_prime = primes_n
                    max_a = a
                    max_b = b
    print 'max_a = %d max_b = %d, a*b = %d, max_prime = %d' % (max_a, max_b, max_a * max_b, max_prime)


def fill_squares(lim):
    squares = []
    for i in range(lim + 1):
        squares.append(i * i)
    return squares


def test(a, b, primes, squares):
    n = 0
    prime = True    
    while prime:
        num = squares[n] + a * n + b
        if num in primes:
            n += 1
        else:
            prime = False
            
    return n


if __name__ == '__main__':
    main()
