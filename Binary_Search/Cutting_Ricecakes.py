import sys

n, m = map(int, input().split()) # 떡 개수, 요청한 떡 길이
lengths = list(map(int, sys.stdin.readline().split())) # 입력 배열 클 땐 sys.stdin.readline 활용(여러줄이면 rstrip 필수)

start = 0
end = max(lengths)

total = 0 # 현재 얻을 수 있는 떡 길이
h = 0

while start<=end:
    mid = (start + end)//2
    total = 0
    
    for l in lengths:
        if l - mid > 0:
            total += (l - mid)
            
    if total >= m:
        h = mid
        start = mid + 1
    else:
        end = mid -1
    
print(h)