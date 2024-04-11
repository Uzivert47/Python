A, B=map(int, input().split())

L=[]
for i in range(1, min(A, B)+1):
    if A%i==0 and B%i==0:
        L.append(i)

print(max(L))

C=A*B/(max(L))

print(int(C))
