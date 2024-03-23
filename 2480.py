user_input=list(map(int,input().split()))

A=user_input[0]
B=user_input[1]
C=user_input[2]

if A==B==C:
    print(10000+1000*A)
elif A==B!=C:
    print(1000+A*100)
elif A==C!=B:
    print(1000+A*100)
elif B==C!=A:
    print(1000+B*100)
else:
    print(max(A,B,C)*100)



