import sys

N=sys.stdin.readline()
answer=list(map(int,(sys.stdin.read().splitlines())))

answer.sort()


for i in answer:
    print(i)







