n, m = map(int,input().split())
weights = list(map(int,input().split()))

case = 0 # 경우의 수
count = [0]*n #무게별 공 개수

for w in weights:
    count[w] += 1
    
for i in range(1, m+1):
    n -= count[i]  #A가 고른 공과 같은 무게인 공 빼기
    case += count[i]*n #A가 고른 공*B가 고를 수 있는 나머지 공
    
print(case)
    