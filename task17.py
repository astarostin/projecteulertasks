import re

data = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
        15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
        19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty',
        50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
        100:'hundred', 1000:'one thousand'}

def main():
    print 'task 17'
    letters = 0
    for i in range(1, 1001): 
        letters += count_letters(num2str(i))
   
    print letters

def num2str(num):    
    if num in data:
        if num == 100:
            return 'one ' + data[num]
        return data[num]
    res = ''
    if num > 100:
        res += data[int(num // 100)] + ' ' + data[100]
        tail = num % 100
        if tail != 0:
            res += ' and '
            if tail in data:
                res += data[tail]
            else:
                res += data[tail - tail % 10] + ' ' + data[tail % 10]
    else:
        res += data[int(num - num % 10)] + ' ' + data[num % 10]
    return res

def count_letters(s):
    s = re.sub(r'\s+', '', s)
    return len(s)
    

if __name__ == '__main__':
    main()
