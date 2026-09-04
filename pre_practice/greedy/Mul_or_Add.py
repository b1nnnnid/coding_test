S = input() #숫자 문자열
num = int(S[0])

for i in range(1, len(S)):
    if num <=1 or int(S[i])<=1:
        num += int(S[i])
    else:
        num *= int(S[i])
        
print(num)