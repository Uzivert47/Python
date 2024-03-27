A=[]
for i in range(9):
    A.append(int(input()))

M=max(A)

print(M)
print(A.index(M)+1)