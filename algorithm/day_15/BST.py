'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key      # 노드의 값
        self.left = None    # 왼쪽 자식 노드를 가리킴
        self.right = None   # 오른쪽 자식 노드를 가리킴

class BinarySearchTree:
    def __init__(self):     # BinarySearchTree 객체가 생성될 때 호출
        self.root = None    # 기본적으로 갖는 루트 노드: None으로 설정해 비어있음을 나타냄

    def insert(self, key):
        '''새로운 노드를 삽입하는 함수'''
        if self.root is None:               # 루트가 비어있으면 (self.root가 None인 경우)
            self.root = Node(key)           # Node(key)를 호출해 좌우 자식이 비어있는 객체를 생성 후 루트로 삼음
        else:                               # 루트가 설정돼 있으면
            self._insert(self.root, key)    # 루트와 키로 삽입 함수 호출

    def _insert(self, node, key):
        if key < node.key:  # 입력받은 값이 만약 현재 바라보는 노드 값보다 작은데,
            if node.left is None:               # 노드의 왼쪽 자식이 비어있으면
                node.left = Node(key)           # 삽입
            else:                               # 왼쪽 자식이 비어있지 않으면 (자식이 있으면)
                self._insert(node.left, key)    # 왼쪽 자식을 바라보는 노드로 해서 재귀 호출
        else:               # 만약 입력받은 값이 현재 바라보는 노드 값보다 작지 않은데,
            if node.right is None:              # 노드의 오른쪽 자식이 비어있으면
                node.right = Node(key)          # 삽입
            else:                               # 오른쪽 자식이 비어있지 않으면 (자식이 있으면)
                self._insert(node.right, key)   # 왼쪽 자식을 바라보는 노드로 해서 재귀 호출

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:         # None이거나 (dummy) 찾고자 하는 key가 노드의 key와 같다면
            return node                             # 노드 반환
        if key < node.key:                          # 현재 바라보는 노드의 값보다 key가 작으면
            return self._search(node.left, key)     # 왼쪽 자식을 바라보는 노드로 해서 search 함수 재호출
        else:                                       # 현재 바라보는 노드의 값보다 key가 작지 않으면
            return self._search(node.right, key)    # 오른쪽 자식을 바라보는 노드로 해서 search 함수 재호출

    def inorder_traversal(self):
        '''중위 순회'''
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node: # 노드가 존재하면
            self._inorder_traversal(node.left)  # 왼쪽 서브트리의 노드를 중위 순회
            print(node.key, end=' ')            # 결과 추가
            self._inorder_traversal(node.right) # 오른쪽 서브 트리의 노드를 중위 순회

####################################################################################

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
