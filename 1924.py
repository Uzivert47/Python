Tag=["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
M,D=map(int, input().split())
if M==3 or M==4:
    D=D-3
elif M==5 or M==6:
    D=D-4
elif M==7 or M==8 or M==9:
    D=D-5
elif M==10 or M==11:
    D=D-6
elif M==12:
    D=D-7
if M>1:
    while True:
        D+=31
        M-=1
        if M==1:
            break
Tags=D%7
print(Tag[Tags])
