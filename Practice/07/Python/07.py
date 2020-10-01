sposob = int( input())
import sys
if abs(sposob) > 1000: sys.exit()
elif sposob > 2: print("Ошибочный ввод")
elif sposob == 1:
    a = int( input())
    b = int( input())
    c = int( input())
    if (a+b) < c: sys.exit()
    if (a+c) < b: sys.exit()
    if (b+c) < a: sys.exit()
    p = (a+b+c)/2
    print("S =", (p*(p-a)*(p-b)*(p-c))**0.5)
elif sposob == 2:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    AB = (((x2-x1)**2 + (y2-y1)**2)**0.5)
    BC = (((x3-x2)**2 + (y3-y2)**2)**0.5)
    AC = (((x3-x1)**2 + (y3-y1)**2)**0.5)
    if (AB+BC) < AC: sys.exit()
    if (AB+AC) < BC: sys.exit()
    if (BC+AC) < AB: sys.exit()
    print("S =", 0.5*abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)))
