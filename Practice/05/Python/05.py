x0 = int( input())
v0 = int( input())
t = int( input())
a = g = 9.8
x = x0 + v0*t - (a*t*t)/2
import sys
if v0 < 0: sys.exit(0)
if t < 0: sys.exit(0)

print(abs(x - x0))
