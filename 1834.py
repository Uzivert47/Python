N=int(input())
L=[]

for i in range(N):
    S=N*i+i
    L.append(S)

print(sum(L))