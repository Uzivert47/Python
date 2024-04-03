A,B,V=list(map(int, input().split()))

distance=V-A
day=A-B

result=distance//day+1

if distance%day!=0:
   result+=1

print(result)