user_input=list(map(int, input().split()))

result=sum(x*x for x in user_input)%10

print(result)

    


