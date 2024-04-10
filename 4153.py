import sys

while True:
    S=list(map(int, sys.stdin.readline().split()))
    SS=sorted(S)
    if S==[0,0,0]:
        break
    if (SS[0]**2+SS[1]**2)==SS[2]**2:
        print("right")
    else:
        print("wrong")
    