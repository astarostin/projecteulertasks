import re
import utils_string


def main():
    print 'task 17'
    letters = 0
    for i in range(1, 1001):
        letters += count_letters(utils_string.num2str(i))

    print letters


def count_letters(s):
    s = re.sub(r'\s+', '', s)
    return len(s)


if __name__ == '__main__':
    main()
