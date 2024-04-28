import sys
N=int(input())
S=list(map(int, sys.stdin.readline().split()))
D=int(input())
count=0
for i in range(N):
    if S[i]>D and S[i]%D==0:
        count+=(S[i]//D)-1
    elif S[i]>D and S[i]%D!=0:
        count+=(S[i]//D)
    elif S[i]==0:
        count-=1
    else:
        pass
print(len(S)*D+count*D)