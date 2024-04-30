N=int(input())
H=[]
W=[]
ranks=[1]*N
for i in range(N):
    A,B=map(int,input().split())
    W.append(A)
    H.append(B)
for j in range(N):
    for k in range(N):
        if W[j]>W[k] and H[j]>H[k]:
            ranks[k]+=1
print(*ranks)