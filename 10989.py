import sys

N=int(sys.stdin.readline())
A=[0]*10001

for b in range(N):
    number=int(sys.stdin.readline())
    A[number]+=1


for c in range(10001):
    for d in range(A[c]):
        print(c)
