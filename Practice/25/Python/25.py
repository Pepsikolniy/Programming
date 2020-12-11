import random as rand
import time
import math
def BozoSort(mass, des = True):
    result = []
    if type(mass[0]) == list:
        for elem in mass:
            result += elem
    else:
        result = mass.copy()
    n = len(result)
    while(is_sorted(result, des) == False):
        for i in range(n-1):
            k, i = rand.randint(0,n-1), rand.randint(0,n-1)
            result[i], result[k] = result[k], result[i]
    return result
def is_sorted(mass, des):
    result = mass
    n = len(result)
    if des:
        for i in range (n-1):
            if result[i] > result[i+1]:
                return False
        return True
    else: 
        for i in range (n-1):
            if result[i] < result[i+1]:
                return False
        return True
def BozoSortF3(a,b,c,des = True):
    return BozoSort([a,b,c], des)
n = int(input())
while True:
    if int(math.sqrt(n)) != float(math.sqrt(n)) : 
        n =int(input("Plese, try again. The sqrt of nuber should be integer\n"))
    else:
        break
na = list(map(int, input().split()))
matrica = []
stroka = []
i = 0
for elem in na:
    stroka.append(elem)
    i +=1
    if i% math.sqrt(n) == 0:
        matrica.append(stroka)
        stroka = []
        i = 0
del stroka, i
del(na[n::])
if len(na) < n: print("Error, try again")
print(' '.join(map(str, BozoSort(na))))
print(' '.join(map(str, BozoSort(na, False))))
print(' '.join(map(str, BozoSort(matrica))))
print(' '.join(map(str, BozoSort(matrica, False))))
print(' '.join(map(str, BozoSortF3(na[0],na[1],na[2]))))
print(' '.join(map(str, BozoSortF3(na[0],na[1],na[2],False))))
