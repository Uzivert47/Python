A,B=map(int, input().split())
L=[]
C=1
while True:
    L.extend([C]*C)
    C+=1
    if len(L)>=B:
        break
print(sum(L[A-1:B]))