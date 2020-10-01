n = int( input())
import sys
if n < 2: sys.exit()
i = 2
bool = False
while i < n:  
    if n % i == 0: bool = True; break
    i += 1
if bool == False: print("Простое")
else: print("Составное")
