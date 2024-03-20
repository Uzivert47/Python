
N=int(input())
T=list(map(int, input().split()))

yeongsik = 0
for A in T:
    fee = (A//30+1) * 10
    yeongsik += fee

minsik = 0
for B in T:
    fee = (B//60+1) * 15
    minsik += fee

if yeongsik>minsik:
    print("M", minsik)

elif minsik>yeongsik:
    print("Y", yeongsik)

else:
    print("Y M", yeongsik)




