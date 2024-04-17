N=int(input())
L=[]
i=1
while i*i+i<=2*N:
    L.append(i)
    i += 1
S=L[-1]
D=(S*S +S)//2

if N==D:
    if S%2==0:
        print(f"{S}/1")
    else:
        print(f"1/{S}")
else:
    O=S+2
    K=N-D
    if O%2==1:
        print(f"{K}/{O-K}")
    else:
        print(f"{O-K}/{K}")