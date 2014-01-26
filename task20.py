def main():
    print 'task 20'
    res = 0
    s = str(fact(100))
    for c in s:
       res += int(c)

    print res

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    main()
