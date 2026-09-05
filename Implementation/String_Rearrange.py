S = sorted(input())
sum = 0
onlystr = ""

for c in S:
    # if c not in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    if c.isalpha():
        onlystr+=c
    else:
        sum += int(c)
        
print(onlystr,sum, sep="")