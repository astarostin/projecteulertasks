data = { 1:1, 2:2, 3:6, 4:24, 5:120,
         6:720, 7:5040, 8:40320, 9:362880, 0:1 }

def main():
    print 'task 34'    
    res = 0
    for i in range(3, 1000000):
        res += test(i)
    print res

def test(n):
    s = 0
    for c in str(n):
        s += data[int(c)]
    if s == n:
        return n
    else:
        return 0

if __name__ == '__main__':
    main()
