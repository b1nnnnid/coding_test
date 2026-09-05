def solution(s):
    answer = len(s)
    
    # 한 글자부터 단위 늘려나가기 
    for step in range(1, len(s)//2+1):
        compressed = ""
        front = s[0:step]
        count = 1
        
        # 그 뒷 문자열 단위 간격으로 순회 
        for j in range(step, len(s), step):
            # 단위 문자열이랑 같으면 압축 횟수 증가
            if front == s[j:j+step]:
                count +=1
            else: # 더이상 압축 못할 때
                compressed += str(count)+front if count >=2 else front
                front = s[j:j+step]
                count = 1
        # 나머지 문자열 처리        
        compressed += str(count) + front if count >=2 else front
        answer = min(answer, len(compressed))
        
    return answer
        
        