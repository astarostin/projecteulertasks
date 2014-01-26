data = [1,2,5,10, 20, 50, 100, 200]
data = sorted(data,reverse=True)
cache = {}

def main():
    print 'task 31'
    total = 200 
    print solve(max(data)+1, total)

def solve(prev, total):
    if (prev, total) in cache:        
        return cache[(prev, total)]
    count = 0
    for d in data:
        if d <= prev:
            if d == total:                
                count += 1
            if d < total:
                count += solve(d, total - d)
    cache[(prev, total)] = count
    return count

if __name__ == '__main__':
    import timeit
    count=1
    print(timeit.timeit("main()", setup="from __main__ import main", number=count) / count)

