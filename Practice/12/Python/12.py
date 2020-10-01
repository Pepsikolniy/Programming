n = int( input())
import sys
if n < 1: sys.exit()
i = 1
x = 1
while i <= n:
    x = x * i
    i += 1
print(x)
