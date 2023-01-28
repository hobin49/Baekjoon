# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.
# 모든 노드가 다 연결은 되어 있지만 일부 간선을 사용하지 않아도 괜찮도록 해준다.
# 최소한의 비용으로 구서오디는 신장 트리를 찾는다.
# 대표적인 최소 신장 트리 알고리즘(크루스칼)
# 그리디 알고리즘
# 동작 과정
# 1. 간선 데이터를 비용에 따라 오름차순 정렬한다
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
# 1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다
# 2) 사이클이 발생하는 경우 최소 신상 트리에 포함시키지 않는다
# 3.모든 간 선에 대하여 2번의 과정을 반복한다.
# 비용순으로 정렬
# 최종적으로 만들어지는 최소신장트리에 포함이 되어있는 간선의 개수는 (전체노드읙 개수 -1) -트리의 특성
# 싸이클 또한 존재하지 않는다.
# 유니온 함수를 사용해서 서로 같은 집합에 속할 수 있도록 한다.

# 특정 원소가 속한 집합을 찾기
# 경로 압축 기법
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# # 노드의 개수와 간선(union 연산)의 개수 입력 받기
# v, e = map(int, input().split())
# # 부모 테이블 초기화하기
# parent = [0] * (v + 1)

# # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
# edges = []
# result = 0

# # 부모 테이블상에서, 부모를 자기 자신으로 칙화
# for i in range(1, v + 1):
#     parent[i] = i

# # 모든 간선에 대한 정보를 입력 받기
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#     edges.append((cost, a, b))

# # 간선을 비용순으로 정렬
# edges.sort()

# # 간선을 하나씩 확인하며
# for edge in edges:
#     cost, a, b = edge
#     # 사이클이 발생하지 않는 경우에만 집합에 포함
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
# print(result)

# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
