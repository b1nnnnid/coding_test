import sys

n = int(input()) # 수열 원소 개수
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(array) - 1
point = -1

while start<=end:
    mid = (start+end)//2

    if array[mid] > mid:
        end = mid -1
    elif array[mid] == mid:
        point = mid
        break
    else:
        start = mid + 1
        
        
print(point)