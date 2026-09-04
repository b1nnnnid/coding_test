S = input()
area1 = 0
area0 = 0


if S[1]==0:
    area0+=1
else:
    area1+=1

# index range 에러가 나면 리스트의 첫 번째 값을 반복문 바깥으로 빼보자
for i in range(len(S)-1):
    if int(S[i]) != int(S[i+1]):
        if int(S[i+1]) == 1:
            area0+=1
        else:
            area1+=1
    
        


print(area1 if area1<area0 else area0)