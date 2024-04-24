S=0
for i in range(5):
    N=int(input())
    if N<40:
        N=40
    S+=N
print(int(S/5))