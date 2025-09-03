'''
    <LIFO - 유효한 괄호 검사> _ 2장 자료구조

    괄호로만 구성된 문자열 s가 주어지면 입력 문자열이 유효한 지 확인한다. '(' ')' '{' '}' '[' ']'
    
    1. 열린 괄호는 동일한 유형의 괄호로 닫힐 것.
    2. 열린 괄호는 올바른 순서로 닫힐 것.
    3. 모든 닫는 괄호에는 동일한 유형의 해당 열린 괄호가 있음.
    
    제약: 1 <= s.length <= 10**4
'''

test_cases = [
    "()",
    "(){}[]",
    "(]",
    "([)]",
    "{[]}"
]


class Solution(object):
    def isValid(self,s):
        
        stack = []
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
            
        return len(stack) == 0
    

def main():
    sol = Solution()
    for s in test_cases:
        print(f"'{s}' : {sol.isValid(s)}")
        
if __name__ == "__main__":
    main()