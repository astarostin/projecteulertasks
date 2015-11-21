import math


def main():
    print 'task 48'
    lim = 1000
    n = 10
    parts = []
    for a in range(1, lim + 1):
        p = power(a, a, n)
        parts.append(p)
    
    print str(sum(parts))[-n:]    


def power(a, b, n):
    val = 1
    for i in range(b):
        val = mult2(val, a, n)
    return val


def mult2(a, b, n):
    return int((a * b) % math.pow(10, n))


def mult(a, b, n):
    a = int(str(a)[-n:])    
    dig_b = []    
    for c in str(b):
        dig_b.append(int(c))
    parts = []
    ind_b = len(dig_b) - 1
    
    while ind_b >= 0 and len(dig_b) - ind_b <= n:
        digit = dig_b[ind_b]                
        s = str(a * digit)[-(n - (len(dig_b) - ind_b) + 1):]
        parts.append(s)
        ind_b -= 1
  
    parts2 = []
    i = 0
    for p in parts:            
        parts2.append(int(p + i * '0'))
        i += 1
    return int(str(sum(parts2))[-n:])


if __name__ == '__main__':
    main()
