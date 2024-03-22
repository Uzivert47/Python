user_input=list(map(int,(input().split())))

N=user_input[0]
m=user_input[1]
M=user_input[2]
T=user_input[3]
R=user_input[4]


X=m

total_mins=0
exercise=0
    
if m+T>M:
    
    print("-1")

else:
    
    while exercise<N:
    
        if X+T<=M:
            X+=T
            exercise+=1
            total_mins+=1

        elif X-R<m:
            X=m
            total_mins+=1

        else:
            X-=R
            total_mins+=1

    print(total_mins)