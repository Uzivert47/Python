import sys
N=int(input())
T=0
for i in range(N):
    T+=int(sys.stdin.readline())
print(T-N+1)