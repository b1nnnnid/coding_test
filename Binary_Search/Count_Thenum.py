import sys

n, x = map(int, input().split()) # 수열 원소 개수, 세려는 원소
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(array) - 1

left_idx, right_idx = len(array), -1 #실제 인덱스와 초깃값 안 겹치게

while start <= end:
    mid = (start + end)//2
    
    if array[mid] >= x:
        left_idx = mid
        end = mid - 1
    else:
        start = mid + 1

start = 0
end = len(array) - 1
    
while start <= end:
    mid = (start + end)//2
    
    if array[mid] <= x:
        right_idx = mid
        start = mid + 1
    else:
        end = mid - 1
    
count = right_idx - left_idx + 1
print(count if count > 0 else -1 )