L=[]
for i in range(7):
    N=int(input())
    if N%2!=0:
        L.append(N)
if L:
    print(sum(L))
    print(min(L))
else:
    print(-1)