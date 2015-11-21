import math


def main():
    print 'task 29'
    numbers = []
    lim = 100
    for a in range(2, lim + 1):
        for b in range(2, lim + 1):
            num = math.pow(a, b)
            if num not in numbers:
                numbers.append(num)

    print len(numbers)


if __name__ == '__main__':
    main()
