A,B=map(int, input().split())
L=[]
for i in range(1,A+1):
    if A%i==0:
        L.append(i)
if len(L)<B:
    print(0)
else:
    print(L[B-1])