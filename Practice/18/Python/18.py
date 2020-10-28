bukavki = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
izvestniyeslova = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]
upavshiebukavki = [0]*26
length = 0
for i in range(len(izvestniyeslova)):
    for j in range(len(izvestniyeslova[i])):
        length += 1
        for q in range(26):
            if izvestniyeslova[i][j] == bukavki[q]:
                upavshiebukavki[q] += 1
slovo = input()
veroyatnost = 1
for i in range(len(slovo)):
    for j in range(26):
        if slovo[i] == bukavki[j]:
            veroyatnost *= upavshiebukavki[j]/length
print(veroyatnost)
    
