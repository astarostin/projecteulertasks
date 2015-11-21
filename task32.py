def main():
    print 'task 32'
    prods = []
    for a in range(1, 10):
        for b in range(1000, 10000):
            prod = test(a, b)
            if prod > 0 and prod not in prods:
                prods.append(prod) 
    for a in range(10, 100):
        for b in range(100, 1000):
            prod = test(a, b)
            if prod > 0 and prod not in prods:
                prods.append(prod)            
    print sum(prods)


def test(a, b):
    prod = a * b
    s = str(a) + str(b) + str(prod)
    if len(s) != 9 or '0' in s:
        return 0
    if '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s:
        return prod
    else:
        return 0
    

if __name__ == '__main__':
    main()
