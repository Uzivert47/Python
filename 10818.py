import sys

N=sys.stdin.readline()
numbers=list(map(int,(sys.stdin.readline().strip().split())))
M=max(numbers)
m=min(numbers)

print(m, M)

