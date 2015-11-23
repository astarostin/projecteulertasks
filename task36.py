
def main():
    print 'task 36'
    res = 0
    for i in range(1000001):
        if is_plndr(str(i)) and is_plndr(to_bin(i)):
            #print i
            res += i

    print res    

def to_bin(n):
    return bin(n)[2:]
    
def is_plndr(s):
    return s == s[::-1]

if __name__ == '__main__':
    main()
