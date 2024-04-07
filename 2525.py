A, B=map(int, input().split())
C=int(input())

if B+C<60:
    print(A, B+C)
else:
    mins=(B+C)%60
    added_hours=(B+C)//60

    if added_hours+A>24:
        added_hours=(added_hours+A)%24
        print(added_hours, mins)
    elif added_hours+A==24:
        print(0, mins)
    else:
        print(A+added_hours, mins)
