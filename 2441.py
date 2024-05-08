N=int(input())
count=0
for i in range(N):
    S=[]
    count=0
    L=list(map(int,input().split()))
    even=[]
    for j in range(7):
        if L[j]%2==0:
            even.append(L[j])
            count+=L[j]
    S.append(count)
    S.append(min(even))
    print(*S)
