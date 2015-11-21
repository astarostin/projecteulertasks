def main():
    print 'task28'
    lim = 1001
    res = 1
    n = 1
    period = 2
    prev = 1
    while n < lim:
        for i in range(4):
            res += prev + period
            prev += period
        period += 2
        n += 2
    print res


if __name__ == '__main__':
    main()
