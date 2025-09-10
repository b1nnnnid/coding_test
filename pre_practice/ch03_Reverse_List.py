'''
    <역방향 연결리스트> _ 3장 리스트(List)
    
    단일 연결 리스트가 주어지면 head 목록을 반전하고 반전된 리스트를 반환한다.
    
    - 입력과 출력 확인
    - 모든 노드에 접근 필요: next로 순차 순회 후 방향 변경
    
    
    제약: 
    - 리스트의 노드 수 범위는 [0, 5000] >>> 5* 10**3 ... O(n**2)는 되도록 피할 것
    - -5000 <= Node.val <= 5000

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            return
        
        last=self.head
        while last.next:
            last=last.next
        new_node = Node(data)
        last.next = new_node
    
    def print_list(self):
        current_node= self.head
        while current_node:
            print(current_node.data, end=" > ")
            current_node=current_node.next
        print("None")
        
        
    def reverseList(self,head):
        prev_node = None #새 리스트의 시작 부분(head 후보)이자 이전 노드드
        current_node = self.head
        
        while current_node: #current가 none이 될 때까지 반복복
            next_node=current_node.next #다음 노드 임시 저장 변수수
            current_node.next=prev_node
            prev_node=current_node
            current_node=next_node
        self.head=prev_node

        
def main():
    list= SingleLinkedList()
    list.append(1)
    list.append(3)
    list.append(5)
    list.append(7)
    list.append(9)
    
    print("주어진 연결리스트: ")
    list.print_list()
    print("\n")
    
    list.reverseList(1) #기본 head값 전달
    print("역방향 연결리스트: ")
    list.print_list()
        
if __name__ == "__main__":
    main()