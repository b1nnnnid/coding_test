'''
    <완주하지 못한 선수> _ 4장 해시테이블(Hash Table)
    
    단 한 명을 제외하고 모든 선수가 마라톤을 완주하였다.
    마라톤 참가자 이름이 담긴 배열 participant, 완주한 선수 배열 completion이 주어질 때,
    완주하지 못한 선수의 이름을 return하도록 solution 함수를 작성하시오.
    
    제약:
    - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하이다. (10**5)
    - completion의 길이는 participant의 길이보다 1 작다.
    - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있다.
    - 참가자 중에는 동명이인이 있을 수 있다.

'''


'''
    -리스트 기반

    def solution(participant, completion):
        for c in completion:
            participant.remove(c)
        return participant[0]
        
        
    >> remove() 리스트 메소드: 인덱스를 순회, 반복문과 사용할 경우 시간 복잡도 상승 O(n**2) 될 수도

'''

#해시테이블 기반...하나씩 값 비교 O(n)
def solution(participant, completion):
    hash_table = {}
    for p in participant:
        hash_table[p] = hash_table.get(p, 0) + 1
        
    for c in completion:
        hash_table[c] -= 1
        
    for p in hash_table:
        if hash_table[p] >  0:
            return p
        

def main():
    
    participant = ["수빈","미주","나은","소라","윤아","연우"]
    completion = ["미주","나은","소라","윤아","연우"]
    
    failer = solution(participant, completion)
    print("완주하지 못한 선수명: "+ failer)
    
    return 0


    
if __name__ =="__main__":
    main()