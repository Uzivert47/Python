import sys
N=int(input())

for i in range(N):
    S=sys.stdin.readline()

    count=0
    score=0

    for char in S:
        if char=="O":
            count+=1
            score+=count
        else:
            count=0
    print(score)