a = int(input())
takoy_nomer_est = False
n = list(map(str, input().split()))
for i in n:
    i = list(i)
    if len(i) != 9 :
        continue
    else :
        if i[0]=='a' and i[4]=='5' and i[5]=='5' and i[6]=='6' and i[7]=='6' and i[8]=='1':
            print(''.join(map(str, i)), end = ' ')
            takoy_nomer_est = True
        
if takoy_nomer_est == False:
    print("-1")
