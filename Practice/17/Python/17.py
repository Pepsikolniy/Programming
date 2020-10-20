black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
b = [0] * 37
chislovipalo = [0] * 37
maximum = 0
sum_black = 0
sum_red = 0
k = 12
game = 0
import sys
while 1:
    game += 1
    n = int( input())
    if n < 0 or n > 36:
        sys.exit(0)
    b[n] += 1
    for i in range(37):
        if b[i] > maximum: maximum = b[i]
    for i in range(37):
        if b[i] == maximum:
            print(i, end = ' ')
    print()
    chislovipalo[n] = game
    for i in range(37):
        if chislovipalo[i] == 0 or (game - chislovipalo[i]) > k:
            print(i, end = ' ')
    print()
    for i in range(18):
        if n == black[i]: sum_black += 1
        elif n == red[i]: sum_red += 1
    print(sum_red, sum_black)
