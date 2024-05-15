N=int(input())
for i in range(N):
    L=list(map(int,input().split()))
    L.sort()
    print(L[-3])