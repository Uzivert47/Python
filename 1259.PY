while True:
    N=input()
    if N=="0":
        break
    L=list(N)
    P=True
    for i in range(len(N)//2):
        if N[i]!=N[len(L)-1-i]:
            P=False
            break
    if P:
        print("yes")
    else:
        print("no")
