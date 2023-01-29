import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


v, e = map(int, input().split())

edges = []
result = 0

# 부모테이블 초기화
parent = [0] * (v + 1)

# 부모테이블에서 부모노드가 자기자신을 가리키도록
for i in range(1, v + 1):
    parent[i] = i


for _ in range(e):
    a, b, c = map(int, input().split())

    edges.append((c, a, b))


edges.sort()


for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
