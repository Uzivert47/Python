N=int(input())

for i in range(N):
    A,B=map(int, input().split())
    L=[]
    for j in range(1,max(A,B)+1):
        if A%j==0 and B%j==0:
            L.append(j)
    print(int(A*B/L[-1]))