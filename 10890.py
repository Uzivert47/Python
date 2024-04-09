S = input()
L = [-1]*26

for i in range(len(S)):
    if L[ord(S[i])-97] == -1:
        L[ord(S[i])-97] = i

print(*L)