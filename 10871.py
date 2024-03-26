numbers=list(map(int, input().split()))
A=list(map(int, input().split()))

N=numbers[0]
X=numbers[1]

answers=[]

for i in range(N):
   K=A[i]

   if K<X:
      answers.append(K)

print(*answers)
    
      
      
