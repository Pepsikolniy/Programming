s, l1, r1, l2, r2 = map(int, input().split())
import sys
x1 = l1
x2 = 0

if x1 + r2 < s:
    x2 = r2
    if r1 + r2 < s:
        print('-1')
        sys.exit()
    else:
        x1 = s - r2
if l1 + l2 > s:
    print('-1')
    sys.exit()
else:
    x2 = s - x1

if s == x1 + x2:
    print(x1)
    print(x2)
