from math import sqrt
def print_factorization(n:int) -> None:
    counter = [0]*int(sqrt(n)+1)
    counterer = 0
    counttho = 0
    while n%2 == 0:
        counttho+=1
        n/=2
    for i in range(3,int(sqrt(n))+1,2):
        while n % i == 0: 
            counter[i] += 1
            n/=i
    if counttho>0: counterer+=1
    for i in counter: 
        if i > 0 : counterer+=1
    if n > 2:
        counterer+=1
        if counterer > 1: 
            print(int(n),'*',sep='',end='')
            counterer-=1
        else: print(int(n), end='', sep='')
    if counttho > 1:
        if counterer>1:
            print("2^",counttho,'*', sep='',end='')
            counterer-=1
        else:print("2^",counttho, sep='',end='')
    for i in range (0,len(counter)):
        if counter[i] == 1:
            if counterer > 1: 
                print(i,'*',end='',sep='')
                counterer -=1
            else: print(i,end='',sep='')
        if counter[i] > 1:
            if counterer > 1:
                print(i,'^',counter[i],'*', sep='',end='')
                counterer -=1
            else:
                print(i,'^',counter[i],end='',sep='')
    print('\n')
print_factorization(n = int(input()))
