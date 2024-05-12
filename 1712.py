A,B,C=map(int, input().split())
X=C-B
if X<=0:
    print("-1")
else:
    print(int(A/X)+1)