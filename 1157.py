import sys

S=sys.stdin.readline().upper()
L=[]
X=[]
for i in range(65, 91):
    if chr(i) in S:
        L.append(S.count(chr(i)))
    else:
        L.append(0)

M=max(L)
count=0

for k in range(len(L)):
    if M==L[k]:
        count+=1

if count>1:
    print("?")
else:
    I=L.index(M)
    print(chr(I+65))