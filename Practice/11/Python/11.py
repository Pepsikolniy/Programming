a = int( input())
b = int( input())
c = a

if b > 0:
    while b > 1:
        a = a * c
        b -= 1
elif b < 0:
    while b < -1:
        a = a * c
        b += 1
    a = 1 / a
else:
    a = 1

print(a)
