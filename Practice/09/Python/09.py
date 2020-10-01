h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))
import sys
if h1 > 23 or h1 < 0: sys.exit()
if h2 > 23 or h2 < 0: sys.exit()
if m1 > 59 or m1 < 0: sys.exit()
if m2 > 59 or m2 < 0: sys.exit()
h1 = h1 * 60
h2 = h2 * 60
m1 = m1 + h1
m2 = m2 + h2
if abs(m1 - m2) < 15: print("Встреча сотоится")
else: print("Встреча не состоится")
