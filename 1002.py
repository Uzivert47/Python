T=int(input())

for i in range(T):
    L=list(map(int, input().split()))
    x1,y1,r1,x2,y2,r2=L[0],L[1],L[2],L[3],L[4],L[5]

    d=((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if d==0 and r1==r2:
        print(-1)
    elif d==r1+r2 or d==abs(r1-r2):
        print(1)
    elif abs(r1-r2)<d<(r1+r2):
        print(2)
    else:
        print(0)
