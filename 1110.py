N=int(input())
if N<10:
        N=10*N
count=0
OG=N
while True:
    L=(N//10)+(N%10)
    N=(N%10)*10+(L%10)
    count+=1
    if N==OG:
        break
print(count)
