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


n, m = map(int, input().split())

parent = [0] * (n + 1)
visited = [[0] * (n + 1)]

for i in range(1, n + 1):
    parent[i] = i


edges = []
total = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    total += c

edges.sort()
result = 0
edge_cnt = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # edge count 해준다.
        edge_cnt += 1


if edge_cnt == n - 1:
    print(total - result)

else:
    print(-1)
