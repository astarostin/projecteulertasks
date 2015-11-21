def main():
    print 'task 25'

    a = 1
    b = 1
    n = 2
    while len(str(b)) < 1000:
        temp = b
        b += a
        a = temp
        n += 1

    print n

if __name__ == '__main__':
    main()
