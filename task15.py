cache = {}

def main():
    print 'Task 15'    
    lim = 20
    print find(0,0, lim + 1, 0)    

def find(i, j, lim, num):    
    if i == lim - 1 and j == lim - 1:
        num += 1
        return num

    if i < lim - 1:
        if (i+1, j) in cache:
            num += cache[(i+1, j)]            
        else:
            old = num
            num = find(i + 1, j, lim, num)
            cache[(i+1, j)] = num - old        
        
    if j < lim - 1:
        if (i, j+1) in cache:
            num += cache[(i, j+1)]            
        else:
            old = num
            num = find(i, j + 1, lim, num)
            cache[(i, j+1)] = num - old            

    return num
    
if __name__ == '__main__':
    main()
