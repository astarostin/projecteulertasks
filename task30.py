import math

powers = {}

def main():
    print 'task 30'
    fill_powers(5)
    res = 0
    for i in range(10, 1000000):
        if test(i):
            res += i
    print res

def test(n):
    s = 0
    for c in str(n):
        s += powers[int(c)]
    return n == s

def fill_powers(n):
    for i in range(10):
        powers[i] = math.pow(i, n)


if __name__ == '__main__':
    main()
