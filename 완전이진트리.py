k = int(input())
nodes = list(map(int, input().split()))
# 빈리스트 생성 k의 크기만큼
answer = [[] for _ in range(k)]

# 재귀방식
def inorder(level, left, right):
    if left == right:
        answer[level].append(nodes[left])
        return None
    # 트리의 root index를 찾아낸다.
    mid = (left + right) // 2

    # 해당 깊이에 해당하는 node를 추가한다.
    # [[3], [], []]
    # [[3], [6], []]
    # [[3], [6], [1]]
    # [[3], [6], [1, 4]]
    # [[3], [6, 2], [1, 4]]
    # [[3], [6, 2], [1, 4, 5]]
    # [[3], [6, 2], [1, 4, 5, 7]]

    # 왼쪽 트리
    # [1,6,4]
    # 왼쪽가 오른쪽 구간은 자식 노드이므로 레빌이 1 증가한다. 출력 왼쪽부터 오른쪽 순서이므로
    inorder(level + 1, left, mid - 1)
    inorder(level + 1, mid + 1, right)
    # 왼쪽 구간부터 방문하면서 레벨 리스트에 넣어준다.
    answer[level].append(nodes[mid])


# 노드의 시작은 0번 노드부터 == len(node) - 1
inorder(0, 0, len(nodes) - 1)

for i in answer:
    print(*i)
