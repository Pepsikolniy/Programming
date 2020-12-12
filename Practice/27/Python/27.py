def sort(massiv):
    result = massiv
    for i in range(1, len(massiv)):
        chis_to_vst = result[i]
        j = i-1
        while j >=0 and result[j] < chis_to_vst:
            result[j+1] = result[j]
            j -= 1
        result[j+1] = chis_to_vst
    return result
n = int(input())
a = list(map(int, input().split()))
if len(a)>n: del a[n::]
elif len(a)<n:print("Try again"), exit()
for i in range(0, n):
    b = [item for item in a[0:i+1]]
    lens = len(b)
    sort(b)
    print(' '.join(map(str, b[-5:len(b)])))
