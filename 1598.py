A,B=map(int, input().split())
A-=1
B-=1
D=abs(B%4-A%4)+abs(B//4-A//4)
print(D)