N=int(input())
X=[]

for M in range(N):
    L=list(map(int, str(M)))
    if M+sum(L)==N:
        X.append(M)

if sum(X)==0:
    print(0)
else:
    print(min(X))