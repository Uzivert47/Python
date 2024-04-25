N=int(input())
X=1
for i in range(1,N+1):
    X*=i
C=str(X)
L=[]
for j in C:
    L.append(j)
count=0
for k in range(1,len(L)+1):
    if L[-k]=="0":
        count+=1
    else:
        break
print(count)