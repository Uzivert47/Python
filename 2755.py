scores = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}
def commercial_round(value, decimals=0):
    multiplier = 10 ** decimals
    result = int(value * multiplier + 0.5) / multiplier
    return result
S=[]
D=[]
N=int(input())
for i in range(N):
    L=input().split()
    credit=int(L[1])
    grade=L[2]
    S.append(credit*scores[grade])
    D.append(credit)
total_scores=sum(S)/sum(D)
R=commercial_round(total_scores, 2)
print("{:.2f}".format(R))