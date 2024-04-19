L=[]
for i in range(4):
    L.append(int(input()))
S=sum(L)
print(S//60)
print(S%60)