codes=list(map(int, input().split()))

if codes[0]<codes[1]<codes[2]<codes[3]<codes[4]<codes[5]<codes[6]<codes[7]:
    print("ascending")
elif codes[0]>codes[1]>codes[2]>codes[3]>codes[4]>codes[5]>codes[6]>codes[7]:
    print("descending")
else:
    print("mixed")
