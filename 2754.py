Grade=list(input())

if Grade[0]=="F":
    print(0.0)

else:
    if Grade[0]=="A":
        score=4.0
    elif Grade[0]=="B":
        score=3.0
    elif Grade[0]=="C":
        score=2.0
    elif Grade[0]=="D":
        score=1.0
    else:
        exit()

    if Grade[1]=="-":
        print(score-0.3)
    elif Grade[1]=="+":
        print(score+0.3)
    else:
        print(score)
