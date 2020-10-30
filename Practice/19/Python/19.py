from itertools import permutations
n = int(input())
bukvi = input()
vivod = []
a = bukvi
if n > len(bukvi):
    for i in range(len(bukvi)):
        bukvi = list(bukvi)
        bukvi = a
        bukvi += bukvi[i]
        for item in permutations(bukvi, n):
            print(''.join(item), end = ' ')
