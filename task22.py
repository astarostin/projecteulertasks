import re

from utils_string import word_value


def main():
    print 'task 22'
    f = open('data/task22.txt', 'rU')
    data = []
    for line in f:
        names = line.split(',')
        for name in names:
            data.append(re.sub(r'"', '', name))

    data = sorted(data)
    i = 1
    total = 0
    for line in data:       
        total += word_value(line) * i
        i += 1

    print total


if __name__ == '__main__':
    main()
