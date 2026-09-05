n = input() #현재 캐릭터 점수 N

middle = int(len(n)/2) # 좌우 반으로 나눌 좌표

left_side = n[:middle]
right_side = n[middle:]
left_sum, right_sum = 0, 0 # 좌우 각 자릿수 총합

for i in range(middle):
    left_sum += int(left_side[i])
    right_sum += int(right_side[i])
    
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")