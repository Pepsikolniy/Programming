n = int(input())
import sys
if n > 10**15 or n < 0: sys.exit()
if n == 0: print (0); sys.exit()
from math import log2
sum = 0
x = 1
Log = 0
while x <= n:
    Log = log2(x)
    if Log == int(Log):
        sum += 1
    x += 1
print(sum)
