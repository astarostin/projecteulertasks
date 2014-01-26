def main():
    print 'task 33'
    prod_a = 0
    prod_b = 0
    for a in range(10,99):
        for b in range(a+1,100):
            if test(a,b):
                print '(%d)/(%d)'%(a,b)
                if prod_a == 0:
                    prod_a = a
                    prod_b = b
                else:
                    prod_a *= a
                    prod_b *= b
    div = gcd(prod_a, prod_b)
    print (prod_b // div)
    #print test(49, 98)

def test(a,b):
    div = gcd(a,b)
    #print div
    a1 = a // div
    b1 = b // div

    a2_str = ''
    b2_str = str(b)
    #print '1: a2_str = %s b2_str = %s' % (a2_str, b2_str)
    has_common = False
    for c in str(a):
        if c != '0':
            if c in str(b):
                has_common = True
                b2_str = b2_str.replace(c, '')
            else:
                a2_str += c
        #print 'c: %s a2_str = %s b2_str = %s' % (c, a2_str, b2_str)
    if not has_common or a2_str == '' or b2_str == '':
        return False
    a2 = int(a2_str)
    b2 = int(b2_str)
    if a2 == 0 or b2 == 0:
        return False
    div2 = gcd(a2, b2)
    a3 = a2 // div2
    b3 = b2 // div2
    #print a3, ' ', b3

    return a1 == a3 and b1 == b3# and a1 != a2 and b1 != b2

def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(b,a)
    if a % b == 0:
        return b
    while rem(a,b) != 0:
        r = rem(a,b)
        a = b
        b = r
    return b

def rem(a, b):
    if a == b:
        return 0
    if a < b:
        rem(b,a)
    if a % b == 0:
        return 0
    i = 1
    while (a - b*i) > b:
        i += 1
    return (a - b*i)

if __name__ == '__main__':
    import timeit
    count=1
    print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)


