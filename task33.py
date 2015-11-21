import utils


def main():
    print 'task 33'
    prod_a = 0
    prod_b = 0
    for a in range(10, 99):
        for b in range(a + 1, 100):
            if test(a, b):
                print '(%d)/(%d)' % (a, b)
                if prod_a == 0:
                    prod_a = a
                    prod_b = b
                else:
                    prod_a *= a
                    prod_b *= b
    div = utils.gcd(prod_a, prod_b)
    print (prod_b // div)


def test(a, b):
    div = utils.gcd(a, b)
    a1 = a // div
    b1 = b // div

    a2_str = ''
    b2_str = str(b)
    has_common = False
    for c in str(a):
        if c != '0':
            if c in str(b):
                has_common = True
                b2_str = b2_str.replace(c, '')
            else:
                a2_str += c
    if not has_common or a2_str == '' or b2_str == '':
        return False
    a2 = int(a2_str)
    b2 = int(b2_str)
    if a2 == 0 or b2 == 0:
        return False
    div2 = utils.gcd(a2, b2)
    a3 = a2 // div2
    b3 = b2 // div2

    return a1 == a3 and b1 == b3


if __name__ == '__main__':
    main()
