T=int(input())

for i in range(T):
    
    x=list(map(int, input().split()))
    H, W, N = x[0], x[1], x[2]

    floor=N%H

    if floor==0:
        floor=H
        door=N//H
    else:
        door=N//H+1
    
    if door<10:
        door="0"+str(door)


    print(str(floor)+str(door))
    
    

   

