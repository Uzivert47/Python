N=int(input())
scores=list(map(int, input().split()))
M=max(scores)
A=[]

for i in range(N):
    K=scores[i]/M*100
    A.append(K)

print(sum(A)/N)
    