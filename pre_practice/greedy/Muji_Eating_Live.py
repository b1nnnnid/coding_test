def solution(food_times, k):
    #전체 음식 먹는 시간이 k보다 작으면 다 먹어서 -1
    if sum(food_times)<k:
        return -1
    
    # 음식 먹는 시간, 번호를 튜플로 저장
    foods = sorted([(time, i+1) for i, time in enumerate(food_times)])
    
    # 남은 음식 개수
    n = len(food_times)
    # 직전에 먹은 음식 시간
    prev =0
    
    # i는 이미 다 먹은 음식 수
    for i, (time, num) in enumerate(foods):
        diff = time - prev #원래 시간 - 이미 먹은 시간
        if diff != 0: #아직 덜 먹었으면
            spend = diff * (n-i)
            # k 전에 한바퀴 돌 수 있으면 수초 써버리기
            if k >= spend:
                k-= spend
                prev = time
            else: #더 이상 한 번에 빼버릴 수 없을 때
                # 남은 음식들만 번호순으로 정렬 후 k번째 반환
                remain= sorted(foods[i:], key=lambda x: x[1])
                return remain[k%(n-i)][1]
            
            
    return -1
    