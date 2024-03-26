N=int(input())
numbers=list(map(int, input().split()))
K=int(input())

count=0

for i in range(N):
    A=numbers[i]
    
    if A==K:
        count+=1

print(count)
        



