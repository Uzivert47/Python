import sys

L=[]

for i in range(10):
    A=int(sys.stdin.readline())
    L.append(A%42)

print(len(set(L)))