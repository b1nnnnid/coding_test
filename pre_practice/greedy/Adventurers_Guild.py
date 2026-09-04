n = int(input()) #모험가의 수
scared = sorted(list(map(int, input().split()))) #공포도 배열
count = 0 #그룹 개수
group = 0 #현재 그룹 인원

for i in scared:
    group+=1
    if group >= i:
        count+=1
        group=0
        
print(count)
