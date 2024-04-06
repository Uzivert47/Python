N=int(input())

count=0
if N==1:
    print(1)
else:
    for i in range(1,N):
        if N>1+(3*i)*(i-1):
            count+=1
        else:
            break
            
        
    print(count+1)
        
    