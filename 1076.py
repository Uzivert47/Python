color_codes = {
    "black": [0, 1],
    "brown": [1, 10],
    "red": [2, 100],
    "orange": [3, 10**3],
    "yellow": [4, 10**4],
    "green": [5, 10**5],
    "blue": [6, 10**6],
    "violet": [7, 10**7],
    "grey": [8, 10**8],
    "white": [9, 10**9]
}


a=input()
b=input()
c=input()

if a in color_codes:
     X=color_codes[a]
     A=X[0]

if b in color_codes:
     Y=color_codes[b]
     B=Y[0]

if c in color_codes:
     Z=color_codes[c]
     C=Z[1]

print((10*A+B)*C)






