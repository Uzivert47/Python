L=[]
for i in range(9):
    L.append(int(input()))
S=sum(L)-100
for j in range(9):
    for k in range(9):
        if L[j]+L[k]==S and j!=k:
            A=j
            B=k
L.pop(A)
L.pop(B)
L.sort()
for l in range(7):
    print(L[l])