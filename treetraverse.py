import sys


input = sys.stdin.readline
# 빈 딕셔너리 생성
tree = {}


t = int(input())

# 입력갑을 받아주고
for _ in range(t):
    root, left, right = input().split()
    # 루트 노드에 왼쪽 자식 노드을 담아준다.
    # {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
    tree[root] = [left, right]


# 전위 순회한 결과
def preorder(root):
    # 만약 루트노드가 .이 아니면
    # A->A[0](B)->B[0](D)->D[0](.)발견 ->D[1](.)발견 -> B[1](.)발견 -> A[1] C -> C[0](E)
    # E[0](.) -> E[1](.) -> C[1] (F) -> F[0] (.) -> F[1] (G)
    # ABDCEFG
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


# 중위 순회
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


# 후위순회
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


# 루트노드는 A
preorder("A")
print()
inorder("A")
print()
postorder("A")
