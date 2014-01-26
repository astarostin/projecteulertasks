def main():
    print 'task 24'
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 1
    lim = 1000000
    finished = False
    while finished != True and count < lim:
        data = next_perm(data)
        count += 1
        finished = data == None

    print data
        

def next_perm(data):
    i = len(data) - 1
    while i > 0 and data[i] < data[i-1]:        
        i -= 1
    if i == 0:
        return None
    tail = data[i:]
    before_tail = data[i-1]
    min_in_tail = 10
    min_in_tail_pos = -1
    
    for j in range(0, len(tail)):
        if tail[j] < min_in_tail and tail[j] > before_tail:
            min_in_tail = tail[j]
            min_in_tail_pos = j

    if min_in_tail_pos != -1:
        data[i-1] = min_in_tail
        tail[min_in_tail_pos] = before_tail
        tail.reverse()
        data[i:] = tail

    return data

if __name__ == '__main__':
    main()
