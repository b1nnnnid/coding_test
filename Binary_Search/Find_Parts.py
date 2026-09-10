n = int(input()) # 보유한 부품 개수
n_nums = sorted(list(map(int, input().split()))) # 보유한 부품 번호

m = int(input()) # 보유 여부를 확인할 부품 개수
m_nums = list(map(int, input().split())) # 보유 여부를 확인할 부품 번호

for i in m_nums:
    start = 0
    end = len(n_nums)
    
    while start<=end:
        mid = (start + end)//2
        if i == n_nums[mid]:
            print("yes")
            break
        elif i < n_nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else: 
        print("no")

