user_input=list(map(int,(input().split())))

N=user_input[0]
L=user_input[1]
D=user_input[2]

listening_time=0
ring_time=0

while True:
   
    if ring_time % (L + 5) < L and ring_time // (L + 5) < N:
        ring_time += D
    else:
        break


print(ring_time)