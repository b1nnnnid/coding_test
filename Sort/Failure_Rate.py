def solution(N, stages):
    fail = [0]*(N+1)
    success = [0]*(N+1)
    
    rate = []
    
    for stage in range(1, N+1):
        for s in stages:
            if s > stage:
                success[stage] += 1
            elif s == stage:
                fail[stage] += 1
                
        if success[stage] == 0 and fail[stage] ==0 :
            rate.append([stage, 0])
        else:
            rate.append([stage, fail[stage]/(fail[stage]+success[stage])])
    
    rate = sorted(rate, key = lambda r: r[1], reverse=True)
    res = []
        
    for i in range(0, N):
        res.append(rate[i][0])
        
    return res