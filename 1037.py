import sys

N=int(input())
L=list(map(int, sys.stdin.readline().split()))
L.sort()

print(L[0]*L[-1])