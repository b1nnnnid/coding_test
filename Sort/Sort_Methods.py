array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
def Selection_Sort(arr):
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[min_idx], arr[i] =  arr[i], arr[min_idx]
        
    return arr


# 삽입 정렬 
def Insertion_Sort(arr):
    for i in range(1, len(arr)): 
        for j in range(i, 0, -1): #좌측으로 한 칸씩 이동
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else: #더 작은 데이터 만나면 멈추고 그 자리 삽입
                break
    return arr


# 퀵 정렬 
def Quick_Sort(arr, start, end):
    if start>= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        # 피벗보다 더 큰 데이터 찾을 때까지
        while left <= end and arr[left] <= arr[pivot]:
            left +=1
        # 피벗보다 더 작은 데이터 찾을 때까지
        while right > start and arr[right] >= arr[pivot]:
            right -=1
        
        # 엇갈리면 피벗이랑 작은 쪽 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 안 엇갈리면 작은 데이터랑 큰 데이터 교체
            arr[left], arr[right] = arr[right], arr[left]
            
        Quick_Sort(arr, start, right-1)
        Quick_Sort(arr, right+1, end)


# 계수 정렬
def Count_Sort(arr):
    # 최댓값 크기 + 1 배열 초기화
    arr_count = [0]*(max(arr) +1)
    sorted = []
    
    for i in range(len(arr)):
        arr_count[arr[i]] += 1
        
    for i in range(len(arr_count)):
        for j in range(arr_count[i]):
            sorted.append(i)
            
    return sorted


print(Selection_Sort(array.copy()))
print(Insertion_Sort(array.copy()))
print(Count_Sort(array.copy()))
print(array)

Quick_Sort(array, 0, len(array)-1)
print(array)


