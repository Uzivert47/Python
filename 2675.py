S=int(input())

for i in range(S):
    A, B=input().split()
    A=int(A)
    K=""

    for x in B:
        K+=x*A

    print(K)
