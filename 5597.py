list_N=[]
a=set(range(1,31))

for k in range(28):
    N=int(input())
    list_N.append(N)
    b=set(list_N)

C=list(a-b)

print(min(C))
print(max(C))

