N=int(input())

A=list(map(int, input().split()))

count=0

for i in range(len(A)):
    if A[i]>1 and all(A[i] % k for k in range(2, int(A[i]**0.5) + 1)):
        count+=1

print(count)

