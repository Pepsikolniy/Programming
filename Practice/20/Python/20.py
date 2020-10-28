n = int(input())
k = int(input())
full_volume = 0
max_bottles = 0
best_drink_name = "asd"
best_bottles = 0
best_price = 0
ostatok = 0
import sys
if k < 1 or n < 0:
    sys.exit(0)
max_volume = 0
for i in range (k):
    name,price,volume = map(str, input().split())
    if n > int(price):
        max_bottles = int(n/int(price))
        full_volume = int(max_bottles * int(volume))
        if full_volume > max_volume:
            max_volume = int(full_volume)
            best_drink_name = name
            best_bottles = int(max_bottles)
            best_price = int(price)
            ostatok = int(n - int(best_price)*best_bottles)
if max_volume == 0:
    print(-1)
else:
    print(best_drink_name, best_bottles, sep = ' ')
    print(max_volume)
    print(ostatok)
