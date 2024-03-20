A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
D=list(map(int, input().split()))


SP=0
a=SP-A[0]
b=a+A[1]
c=b-B[0]
d=c+B[1]
e=d-C[0]
f=e+C[1]
g=f-D[0]
h=g+D[1]

print(max(a,b,c,d,e,f,g,h))
