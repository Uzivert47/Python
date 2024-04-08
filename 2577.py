A=int(input())
B=int(input())
C=int(input())
N=A*B*C
K=[]

for a in str(N):
    K.append(int(a))

for b in range(10):
    X=K.count(b)
    print(X)