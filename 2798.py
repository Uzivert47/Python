A, B=map(int, input().split())
C=list(map(int, input().split()))

S=[]
for a in range(A):
    C[a]
    for b in range(A):
        C[b]
        for c in range(A):
            C[c]

            if C[a]+C[b]+C[c]<=B and a!=b and b!=c and c!=a:
                
                S.append(C[a]+C[b]+C[c])

print(max(S))