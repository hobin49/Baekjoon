# k = int(input())
# nodes = list(map(int, input().split()))
# # 빈리스트 생성 k의 크기만큼
# answer = [[] for _ in range(k)]


# def inorder(level, left, right):
#     if left == right:
#         # nodes의 인덱스 [0, 2, 4, 6]
#         answer[level].append(nodes[left])
#         return None
#     # 트리의 root노드를 찾는다.
#     mid = (left + right) // 2
#     #    3
#     #  2   6
#     # 1 4 5 7
# 해당 깊이에 해당하는 node를 추가한다.
# 1. [[], [], [1]] # 왼쪽 자식 노드
# 2. [[], [], [1, 4]] #오른쪽 자식 노드
# 3. [[], [6], [1, 4]] #부모 노드
# 4. [[], [6], [1, 4, 5]] #왼쪽 자식 노드
# 5. [[], [6], [1, 4, 5, 7]] #오른쪽 자식 노드
# 6. [[], [2, 6], [1, 4, 5, 7]] # 부모 노드
# 7. [[3], [2, 6], [1, 4, 5, 7]] # 루트 노드

#     # 왼쪽 구간
#     # 왼쪽가 오른쪽 구간은 자식 노드이므로 레빌이 1 증가한다. 출력 왼쪽부터 오른쪽 순서이므로
#     inorder(level + 1, left, mid - 1)
#     # 오른쪽 구간
#     inorder(level + 1, mid + 1, right)
#     # 왼쪽 구간부터 방문하면서 레벨 리스트에 넣어준다.
#     answer[level].append(nodes[mid])


# # 노드의 시작은 0번 노드부터 == len(node) - 1
# inorder(0, 0, len(nodes) - 1)
# # unpacking
# for i in answer:
#     print(*i)

# 입력값 받아주고
n = int(input())
lst = list(map(int, input().split()))
# [0, 0, 0, 0, 0, 0, 0]
check = [0] * (2**n - 1)
answer = []

#    3
#  2   6
# 1 4 5 7
# 1. [[1], [], []]
# 2. [[1, 4], [], []]
# 3. [[1, 4, 5], [], []]
# 4. [[1, 4, 5, 7], [], []]
# 5. [[1, 4, 5, 7], [6], []]
# 6. [[1, 4, 5, 7], [6, 2], []]
# 7. [[1, 4, 5, 7], [6, 2], [3]]

# 트리레벨 만큼 돌아주면서
for _ in range(n):
    # 임시리스트
    temp = []
    # 방문시 시용
    flag = True
    # enumerate 함수 사용해서 (인덱스, 요소)
    for i, l in enumerate(lst):
        # 만약 True이고 방문하지 않았으면
        if flag and check[i] == 0:
            # 방문표시 해주고
            check[i] = 1
            # 임시 리스트에 인덱스에 해당하는 요소를 넣어준다.
            temp.append(l)
            # 방문표시 해주고
            flag = False
        # 만약에 False이고 방문하지 않은 곳이면 True로 바꿔주고 다시 if문으로 가서 돌을 수 있게 한다.
        elif not flag and check[i] == 0:
            flag = True
    # 임시리스트를 리스트에 넣어준다.
    answer.append(temp)

# [[1, 4, 5, 7], [6, 2], [3]]
# reversed해줘서 리스트를 거꾸로 뒤집는다.
for a in reversed(answer):
    print(*a)
